"""
Automated Companion Guide Generator for Chandamama Kathalu (Telugu)
Target Audience: 8-year-old reader (Grade 3)
Generates: <PDF_NAME>-AINotes.md alongside each PDF file.
"""

import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import APIError

# Ensure terminal stdout handles Telugu characters cleanly on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Load environment variables from .env file if present
load_dotenv()

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_DIR = Path(r"D:\GoogleDriveSync\VirataHomeSchool\2. ClassMaterial\Others\StoryBooks\Telugu\ChandamamaKathalu\ChandamamaTelugu1947-2006")
MODEL_ID = "gemini-3.8-flash"  # Multimodal model supporting native PDF processing with high OCR quality
MAX_RETRIES = 3

# ---------------------------------------------------------------------------
# System Instructions & Enhanced Prompt for 8-Year-Old Readers
# ---------------------------------------------------------------------------
SYSTEM_INSTRUCTION = """You are an expert Telugu teacher and children's literature specialist assisting an 8-year-old Grade 3 student.
Your task is to analyze historical Chandamama Telugu magazines and generate a comprehensive, engaging companion study guide.
The output must be formatted in clean GitHub Markdown."""

PROMPT_TEMPLATE = """You are given a complete scanned issue of the Telugu children's magazine 'Chandamama'.
An 8-year-old student (Grade 3) who is learning Telugu is reading this magazine. 
Because the language used in Chandamama (especially older issues) includes classical, literary, and formal Telugu words, the student needs an elaborate companion guide to understand, enjoy, and learn from every story.

Please thoroughly analyze the entire issue from first page to last page and produce a companion guide in Markdown with the following structure:

# 🌙 చందమామ (Chandamama) - [Month, Year] Issue
## Companion Guide for Young Readers (8-Year-Old Edition / Grade 3)

### 📋 Table of Contents & Stories in this Issue
List all stories, poems, serial features, and articles with their approximate page numbers.

---

For EACH story, poem, serial episode, and feature in the magazine, create a dedicated section following this exact layout:

## [Number]. [Telugu Title] ([English Title Translation])
**Pages:** [Page range] | **Author:** [Author name if given, else 'Traditional / Folk Tale / Not Mentioned']

### 📖 విస్తృత పదకోశం - పదాలు & అర్థాలు (Elaborate Vocabulary)
Extract an exhaustive, elaborate list of all difficult, literary, uncommon, or formal Telugu words from this story.
Provide a clean Markdown table with:
| తెలుగు పదం (Word) | లిప్యంతరీకరణ (Transliteration) | సులువైన తెలుగు అర్థం (Simple Telugu) | English Meaning (Grade-3 Level) | కథలో వాడకం (Context / Usage) |
|---|---|---|---|---|
*Ensure the simple Telugu uses everyday words an 8-year-old child understands.*
*Make the list very thorough and elaborate—include 10 to 25 words per story so the child never gets stuck.*

### 📝 కథ సారాంశం (English Story Summary)
Write a clear, vibrant, and engaging story summary in 2 to 4 paragraphs using simple, lively English suitable for an 8-year-old reader. Capture the beginning, the plot twist/conflict, and the resolution.

### 🌟 నీతి / ముఖ్య సందేశం (Moral / Key Takeaway)
1 to 2 clear sentences explaining the life lesson, wisdom, or humor in the story.

### 💡 ఆలోచించండి (Questions to Think & Discuss)
1 to 2 fun, thought-provoking questions for parents and child to discuss together after reading.

---

### Important Guidelines:
1. Cover EVERY story, poem, fable, and feature in the magazine without skipping any.
2. Be extremely thorough with the vocabulary lists.
3. Keep the tone warm, encouraging, and educational.
"""

def get_client() -> genai.Client:
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("\n" + "!" * 70)
        print("[ERROR] GEMINI_API_KEY (or GOOGLE_API_KEY) is not set!")
        print("Please provide your API key in your '.env' file: GEMINI_API_KEY=your_key_here")
        print("!" * 70 + "\n")
        sys.exit(1)
    return genai.Client(api_key=api_key)

def process_single_pdf(client: genai.Client, pdf_path: Path, force: bool = False) -> bool:
    output_md_path = pdf_path.with_name(f"{pdf_path.stem}-AINotes.md")
    
    if output_md_path.exists() and not force:
        print(f"[SKIP] Notes already exist: {output_md_path.name}")
        return False

    print(f"\n{'='*70}")
    print(f"[PROCESSING] {pdf_path.name} ({pdf_path.stat().st_size / (1024*1024):.1f} MB)")
    print(f"Path: {pdf_path}")
    
    for attempt in range(1, MAX_RETRIES + 1):
        uploaded_file = None
        try:
            # 1. Upload scanned PDF via Gemini File API
            print(f"Uploading PDF to Gemini File API (Attempt {attempt}/{MAX_RETRIES})...")
            uploaded_file = client.files.upload(
                file=str(pdf_path),
                config=types.UploadFileConfig(mime_type="application/pdf")
            )
            print(f"Uploaded successfully. File name: {uploaded_file.name}")

            # 2. Wait until file state is ACTIVE
            print("Verifying file processing state on server...")
            file_info = client.files.get(name=uploaded_file.name)
            while file_info.state.name == "PROCESSING":
                print("  File is still processing on Google servers, waiting 5 seconds...")
                time.sleep(5)
                file_info = client.files.get(name=uploaded_file.name)

            if file_info.state.name != "ACTIVE":
                raise RuntimeError(f"File state is not ACTIVE: {file_info.state.name}")

            # 3. Generate Content using Gemini
            print(f"Generating companion guide using {MODEL_ID}...")
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=[file_info, PROMPT_TEMPLATE],
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    temperature=0.3,
                )
            )
            
            # 4. Write Markdown file
            with open(output_md_path, "w", encoding="utf-8") as f:
                f.write(response.text)
                
            print(f"[SUCCESS] Saved notes to: {output_md_path.name}")
            return True

        except Exception as e:
            err_msg = str(e)
            print(f"[WARN] Attempt {attempt} failed: {err_msg}")
            
            # Retry with backoff if server is busy or transient error
            if attempt < MAX_RETRIES:
                wait_seconds = 10 * attempt
                print(f"Retrying in {wait_seconds} seconds...")
                time.sleep(wait_seconds)
            else:
                print(f"[ERROR] All {MAX_RETRIES} attempts failed for {pdf_path.name}")
                return False
                
        finally:
            # Clean up uploaded file on Google servers to conserve storage quota
            if uploaded_file:
                try:
                    client.files.delete(name=uploaded_file.name)
                except Exception:
                    pass

def process_all_files(client: genai.Client | None, root_dir: Path, dry_run: bool = False, max_files: int | None = None):
    pdf_files = sorted(list(root_dir.rglob("*.pdf")))
    total_files = len(pdf_files)
    print(f"Discovered {total_files} PDF files under {root_dir}")

    existing_notes = list(root_dir.rglob("*-AINotes.md"))
    print(f"Existing notes files found: {len(existing_notes)}")
    remaining = total_files - len(existing_notes)
    print(f"Remaining files to process: {remaining}")

    if dry_run:
        print("\n[DRY RUN] Sample of pending files:")
        count = 0
        for pdf in pdf_files:
            md_file = pdf.with_name(f"{pdf.stem}-AINotes.md")
            if not md_file.exists():
                print(f"  - {pdf.parent.name}/{pdf.name}")
                count += 1
                if count >= 10:
                    break
        return

    processed_count = 0
    for idx, pdf in enumerate(pdf_files, start=1):
        md_file = pdf.with_name(f"{pdf.stem}-AINotes.md")
        if md_file.exists():
            continue
            
        print(f"\n[{idx}/{total_files}] Starting: {pdf.parent.name}/{pdf.name}")
        success = process_single_pdf(client, pdf)
        if success:
            processed_count += 1
            # Respect rate limits between files
            time.sleep(5)
            
        if max_files and processed_count >= max_files:
            print(f"\nReached specified limit of {max_files} processed files.")
            break

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate Chandamama Telugu AI Companion Notes")
    parser.add_argument("--test-one", action="store_true", help="Process only the first missing PDF for evaluation")
    parser.add_argument("--dry-run", action="store_true", help="List files without calling API")
    parser.add_argument("--max", type=int, default=None, help="Maximum number of files to process in this run")
    args = parser.parse_args()

    if args.dry_run:
        process_all_files(None, BASE_DIR, dry_run=True)
        sys.exit(0)

    client = get_client()

    if args.test_one:
        print("Mode: Single File Test for prompt evaluation.")
        process_all_files(client, BASE_DIR, max_files=1)
    else:
        process_all_files(client, BASE_DIR, dry_run=args.dry_run, max_files=args.max)
