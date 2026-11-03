"""
Automated Companion Guide Generator for Chandamama Kathalu (Telugu)
Target Audience: 8-year-old reader (Grade 3 - Early/Beginner Vocabulary Level)
Workflow: Two-stage Chapter-by-Chapter extraction with automatic Printed vs PDF Page Offset Detection.
Generates: <PDF_NAME>-AINotes.md alongside each PDF file.

# How to run?
# For a single file of your choice:
.venv\Scripts\python.exe 1.TeluguFiles-AINotes.py --file Chandamama-1947-8.pdf --force
# For all ~700 files in a loop:
.venv\Scripts\python.exe 1.TeluguFiles-AINotes.py --all
"""

import os
import sys
import time
import json
import argparse
import tempfile
from pathlib import Path
from datetime import datetime
import pypdf
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Ensure terminal stdout handles Telugu characters cleanly on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Load environment variables (.env)
load_dotenv()

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_DIR = Path(r"D:\GoogleDriveSync\VirataHomeSchool\2. ClassMaterial\Others\StoryBooks\Telugu\ChandamamaKathalu\ChandamamaTelugu1947-2006")

# Only active, valid models for new Google GenAI accounts.
# gemini-2.5-flash is retired (returns 404 for new keys).
MODELS = ["gemini-3.8-flash", "gemini-3.5-flash"]
MAX_RETRIES = 5

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------
TOC_PROMPT = """You are analyzing the opening pages of a scanned vintage Telugu children's magazine 'Chandamama' (చందమామ).
Find the Table of Contents / Index (విషయ సూచిక / చదువుకోండి).

Extract the list of ALL stories, poems, serial features, and articles.
Return a valid JSON array of objects with the following keys:
- "number": (integer) 1, 2, 3...
- "telugu_title": (string) The Telugu title as printed
- "english_title": (string) English translation of the title
- "author": (string or null) Author name if listed, else null
- "printed_start_page": (integer) The PRINTED book page number shown in the index
- "printed_end_page": (integer) The PRINTED book ending page number (infer from next story's printed_start_page if not shown)

Output ONLY raw valid JSON (no markdown formatting, no code fences, no extra text).
"""

CHAPTER_PROMPT_TEMPLATE = """You are an expert Telugu language teacher and children's literature specialist creating a companion study guide for an 8-year-old Grade 3 student.
The student has an early/beginner Telugu vocabulary and is reading this story from 'Chandamama' (చందమామ).

Story to analyze:
- Story Number: {number}
- Telugu Title: {telugu_title}
- English Title: {english_title}
- Author: {author}
- Book Pages: {printed_start_page} to {printed_end_page} (PDF Pages: {pdf_start_page} to {pdf_end_page})

Please analyze the attached pages of this story and generate a comprehensive study guide section in clean Markdown:

## {number}. {telugu_title} ({english_title})
**Printed Book Pages:** {printed_start_page}–{printed_end_page} (PDF Pages: {pdf_start_page}–{pdf_end_page}) | **Author:** {author}

### 📖 విస్తృత పదకోశం - పదాలు & అర్థాలు (Comprehensive Vocabulary)
IMPORTANT VOCABULARY INSTRUCTIONS FOR AN 8-YEAR-OLD BEGINNER:
Assume a beginner/early level of Telugu vocabulary. Do NOT provide only 5 to 10 words.
Extract an exhaustive, very generous list of words (aim for 25 to 40+ words if present in the story text).
Include:
1. Classical, formal, or literary Telugu words (ప్రాచీన / గ్రాంథిక పదాలు)
2. Compound words (సమాసాలు / సంధి పదాలు)
3. Action verbs, descriptive adjectives, emotional words, and idioms (జాతీయాలు / సామెతలు)
4. Traditional household, nature, village, animal, food, or cultural items that a Grade 3 child might not encounter in modern life.

Format as a Markdown table:
| క్రమ సంఖ్య (No.) | తెలుగు పదం (Word) | లిప్యంతరీకరణ (Transliteration) | సులువైన తెలుగు అర్థం (Simple Telugu) | English Meaning (Simple Grade-3 Level) | కథలో వాక్యం / సందర్భం (Sentence / Context from Story) |
|---|---|---|---|---|---|
*Ensure the Simple Telugu uses everyday words an 8-year-old child understands.*

### 📝 కథ సారాంశం (English Story Summary)
Write a clear, vibrant, and engaging story summary in 2 to 3 paragraphs using simple, lively English suitable for an 8-year-old reader. Capture the beginning, the plot conflict/twist, and the ending.

### 🌟 నీతి / ముఖ్య సందేశం (Moral / Key Takeaway)
Provide 1 to 2 clear sentences in both Telugu and English explaining the moral, wisdom, or humor in the story.

### 💡 ఆలోచించండి (Questions to Think & Discuss)
Provide 2 fun, thought-provoking questions (in both Telugu and English) for parents and child to discuss together after reading.

---
"""

# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------
def get_client() -> genai.Client:
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("\n" + "!" * 70)
        print("[ERROR] GEMINI_API_KEY is not set in environment or .env file!")
        print("Please ensure your API key is in the '.env' file in this folder:")
        print("GEMINI_API_KEY=your_key_here")
        print("!" * 70 + "\n")
        sys.exit(1)
    return genai.Client(api_key=api_key)

def upload_and_wait(client: genai.Client, file_path: str) -> types.File:
    uploaded = client.files.upload(
        file=file_path,
        config=types.UploadFileConfig(mime_type="application/pdf")
    )
    file_info = client.files.get(name=uploaded.name)
    while file_info.state.name == "PROCESSING":
        time.sleep(2)
        file_info = client.files.get(name=uploaded.name)
        
    if file_info.state.name != "ACTIVE":
        raise RuntimeError(f"Uploaded file failed to become ACTIVE: {file_info.state.name}")
    return file_info

def generate_with_fallback(client: genai.Client, contents: list, config: types.GenerateContentConfig):
    """
    Tries valid models in order of priority (newest to oldest).
    If a 404 occurs, that model is permanently dropped.
    If 429/quota occurs, it cycles to the next model.
    Will loop until a response is received, backing off if all models hit temporary limits.
    """
    cycle_count = 0
    while True:
        cycle_count += 1
        for model_name in list(MODELS):
            for attempt in range(1, 3):
                try:
                    resp = client.models.generate_content(
                        model=model_name,
                        contents=contents,
                        config=config
                    )
                    return resp, model_name
                except Exception as e:
                    err_str = str(e)
                    
                    # 404: Model not available for this account -> drop it from candidate list
                    if "404" in err_str or "NOT_FOUND" in err_str:
                        print(f"    [404 NOT_FOUND] Model '{model_name}' is not supported. Removing from list.")
                        if model_name in MODELS:
                            MODELS.remove(model_name)
                        break

                    # 429 / Quota: Try next candidate model
                    if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                        print(f"    [QUOTA] Model '{model_name}' quota reached. Switching to next model...")
                        break

                    # 503 / Temporary server congestion: brief backoff
                    print(f"    [RETRY] '{model_name}' attempt {attempt} failed ({err_str[:70]}...). Waiting 5s...")
                    time.sleep(5)

        # If all candidate models were busy or rate-limited in this cycle, pause and retry
        wait_seconds = min(30 * cycle_count, 120)
        print(f"  [WAIT] All models currently rate-limited or busy. Pausing for {wait_seconds}s before retrying this chapter...")
        time.sleep(wait_seconds)

def detect_page_offset(client: genai.Client, reader: pypdf.PdfReader) -> tuple[int, str]:
    """
    Detects the offset between 1-indexed PDF page numbers and printed book page numbers:
    pdf_page_number = printed_page_number + offset
    """
    total_pages = len(reader.pages)
    check_count = min(10, total_pages)
    
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp_name = tmp.name

    used_model = MODELS[0]
    try:
        writer = pypdf.PdfWriter()
        for i in range(check_count):
            writer.add_page(reader.pages[i])
        with open(tmp_name, "wb") as f_out:
            writer.write(f_out)

        file_ref = upload_and_wait(client, tmp_name)
        try:
            prompt = """Analyze these opening 10 pages of the PDF.
Look for the page where the main stories or poems start (or where printed page numbers 1, 2, 3, 4, 5, 6, 7, 8 appear at the bottom or top corners).
Find at least one page with a clearly visible printed page number.
Return a JSON object:
{
  "pdf_page_number": <1-indexed position in this PDF slice, integer>,
  "printed_book_page_number": <the printed page number visible on that page, integer>
}
Output ONLY raw valid JSON."""

            resp, used_model = generate_with_fallback(
                client,
                contents=[file_ref, prompt],
                config=types.GenerateContentConfig(response_mime_type="application/json", temperature=0.1)
            )
            data = json.loads(resp.text)
            pdf_p = data.get("pdf_page_number")
            printed_p = data.get("printed_book_page_number")
            if pdf_p and printed_p:
                offset = pdf_p - printed_p
                print(f"  [PAGE OFFSET DETECTED] Printed page {printed_p} corresponds to PDF page {pdf_p} (Offset = {offset:+d}) [via {used_model}]")
                return offset, used_model
        finally:
            try:
                client.files.delete(name=file_ref.name)
            except Exception:
                pass
    except Exception as e:
        print(f"  [WARN] Automatic offset detection encountered: {e}. Defaulting to offset +2.")
    finally:
        if os.path.exists(tmp_name):
            try:
                os.remove(tmp_name)
            except Exception:
                pass

    return 2, used_model

def extract_toc(client: genai.Client, pdf_path: Path, reader: pypdf.PdfReader) -> tuple[list, str]:
    """Extracts Table of Contents by analyzing the opening pages."""
    total_pages = len(reader.pages)
    pages_to_check = min(8, total_pages)
    
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp_name = tmp.name
        
    used_model = MODELS[0]
    try:
        writer = pypdf.PdfWriter()
        for i in range(pages_to_check):
            writer.add_page(reader.pages[i])
        with open(tmp_name, "wb") as f_out:
            writer.write(f_out)
            
        file_ref = upload_and_wait(client, tmp_name)
        try:
            resp, used_model = generate_with_fallback(
                client,
                contents=[file_ref, TOC_PROMPT],
                config=types.GenerateContentConfig(response_mime_type="application/json", temperature=0.1)
            )
            data = json.loads(resp.text)
            if isinstance(data, list) and len(data) > 0:
                return data, used_model
        finally:
            try:
                client.files.delete(name=file_ref.name)
            except Exception:
                pass
    except Exception as e:
        print(f"  [WARN] TOC extraction encountered an issue: {e}")
    finally:
        if os.path.exists(tmp_name):
            try:
                os.remove(tmp_name)
            except Exception:
                pass

    # Fallback: Divide into 4-page chunks if TOC not found
    print("  [INFO] Generating chapter slices automatically (4 pages per chunk)...")
    fallback_toc = []
    chunk_size = 4
    for idx, start_p in enumerate(range(1, total_pages + 1, chunk_size), start=1):
        end_p = min(start_p + chunk_size - 1, total_pages)
        fallback_toc.append({
            "number": idx,
            "telugu_title": f"భాగం {idx} (పేజీలు {start_p}-{end_p})",
            "english_title": f"Section {idx} (Pages {start_p}-{end_p})",
            "author": "Chandamama",
            "printed_start_page": start_p,
            "printed_end_page": end_p
        })
    return fallback_toc, used_model

def process_chapter(client: genai.Client, reader: pypdf.PdfReader, chapter: dict, offset: int) -> tuple[str, str]:
    """Slices the EXACT PDF pages corresponding to the printed story pages and generates detailed notes."""
    total_pdf_pages = len(reader.pages)
    
    printed_sp = chapter.get("printed_start_page") or chapter.get("start_page") or 1
    printed_ep = chapter.get("printed_end_page") or chapter.get("end_page") or (printed_sp + 2)
    
    # Accurate page translation: PDF page = printed page + offset
    pdf_start = max(1, min(total_pdf_pages, printed_sp + offset))
    pdf_end = max(pdf_start, min(total_pdf_pages, printed_ep + offset))
    
    # 0-indexed bounds for pypdf slicing
    start_idx = pdf_start - 1
    end_idx = pdf_end
    
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp_name = tmp.name

    try:
        writer = pypdf.PdfWriter()
        for i in range(start_idx, end_idx):
            writer.add_page(reader.pages[i])
        with open(tmp_name, "wb") as f_out:
            writer.write(f_out)

        file_ref = upload_and_wait(client, tmp_name)
        try:
            prompt = CHAPTER_PROMPT_TEMPLATE.format(
                number=chapter.get("number", 1),
                telugu_title=chapter.get("telugu_title", "కథ"),
                english_title=chapter.get("english_title", "Story"),
                author=chapter.get("author") or "Traditional / Not Mentioned",
                printed_start_page=printed_sp,
                printed_end_page=printed_ep,
                pdf_start_page=pdf_start,
                pdf_end_page=pdf_end
            )

            resp, used_model = generate_with_fallback(
                client,
                contents=[file_ref, prompt],
                config=types.GenerateContentConfig(temperature=0.2)
            )
            return resp.text, used_model
        finally:
            try:
                client.files.delete(name=file_ref.name)
            except Exception:
                pass
    finally:
        if os.path.exists(tmp_name):
            try:
                os.remove(tmp_name)
            except Exception:
                pass

def process_book_chapter_by_chapter(client: genai.Client, pdf_path: Path, force: bool = False) -> bool:
    output_md_path = pdf_path.with_name(f"{pdf_path.stem}-AINotes.md")

    if output_md_path.exists() and not force:
        print(f"[SKIP] Notes already exist: {output_md_path.name}")
        return False

    print(f"\n{'='*75}")
    print(f"[PROCESSING ISSUE] {pdf_path.parent.name}/{pdf_path.name} ({pdf_path.stat().st_size / (1024*1024):.1f} MB)")
    print(f"Output: {output_md_path.name}")

    try:
        reader = pypdf.PdfReader(str(pdf_path))
        total_pages = len(reader.pages)
        print(f"Total Pages in PDF: {total_pages}")

        # Track models utilized across chapters
        models_used = set()

        # Step 1: Detect Printed Page vs PDF Page Offset
        offset, offset_model = detect_page_offset(client, reader)
        models_used.add(offset_model)

        # Step 2: Extract Table of Contents
        print("Extracting Table of Contents / Chapters...")
        toc, toc_model = extract_toc(client, pdf_path, reader)
        models_used.add(toc_model)
        print(f"Found {len(toc)} stories/features in this issue.")

        # Write Initial Header & Table of Contents into Markdown
        issue_title = pdf_path.stem.replace("Chandamama-", "Chandamama ")
        generated_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(f"# 🌙 చందమామ ({issue_title})\n")
            f.write("## Companion Study Guide for Young Readers (8-Year-Old Edition / Grade 3)\n\n")
            f.write(f"> **Metadata for Reference:**  \n")
            f.write(f"> - **Generated on:** `{generated_date}`  \n")
            f.write(f"> - **Active AI Models:** `{' → '.join(MODELS)}`  \n")
            f.write(f"> - **Detected Page Offset:** `PDF Page = Book Page + {offset}`  \n\n")
            f.write("ఈ సంచికలోని కథలు, గేయాలు, శీర్షికల విస్తృత పదకోశం మరియు కథా సారాంశాల సమగ్ర గైడ్.\n\n")
            f.write("### 📋 విషయ సూచిక (Table of Contents & Stories in this Issue)\n\n")
            for item in toc:
                num = item.get("number", "")
                t_title = item.get("telugu_title", "")
                e_title = item.get("english_title", "")
                sp = item.get("printed_start_page") or item.get("start_page", "")
                ep = item.get("printed_end_page") or item.get("end_page", "")
                pg_str = f" [పుస్తకం పేజీలు {sp}–{ep}]" if sp and ep else ""
                f.write(f"{num}. **{t_title}** (*{e_title}*){pg_str}\n")
            f.write("\n---\n\n")

        # Step 3: Process Chapter by Chapter (NO CHAPTER IS SKIPPED: Must complete before advancing)
        for idx, chapter in enumerate(toc, start=1):
            t_title = chapter.get("telugu_title", "కథ")
            e_title = chapter.get("english_title", "Story")
            print(f"  [{idx}/{len(toc)}] Analyzing: {t_title} ({e_title})...", flush=True)
            
            # Persistent retry loop: never skips to the next chapter until this chapter succeeds
            chapter_done = False
            while not chapter_done:
                try:
                    chapter_md, chap_model = process_chapter(client, reader, chapter, offset)
                    models_used.add(chap_model)
                    with open(output_md_path, "a", encoding="utf-8") as f:
                        f.write(f"<!-- AI Model used for chapter {idx}: {chap_model} -->\n")
                        f.write(chapter_md + "\n\n")
                    print(f"  [{idx}/{len(toc)}] ✓ Saved notes for '{t_title}' (Model: {chap_model})", flush=True)
                    chapter_done = True
                except Exception as e:
                    print(f"  [{idx}/{len(toc)}] Error on '{t_title}': {e}. Waiting 15s to retry this exact chapter...", flush=True)
                    time.sleep(15)

            # Polite rate limiting between chapters
            time.sleep(4)

        # Append final metadata footer showing summary of AI models used
        with open(output_md_path, "a", encoding="utf-8") as f:
            f.write("\n---\n")
            f.write(f"*AI Generation Summary: Processed with Google GenAI ({', '.join(sorted(models_used))})*\n")

        print(f"\n[COMPLETED] Successfully generated complete guide: {output_md_path.name}")
        return True

    except Exception as e:
        print(f"[ERROR] Failed to process {pdf_path.name}: {e}")
        return False

# ---------------------------------------------------------------------------
# Main Runner & CLI
# ---------------------------------------------------------------------------
def find_matching_pdf(root_dir: Path, query: str) -> Path | None:
    query = query.strip().replace("/", "\\")
    p = Path(query)
    if p.exists() and p.suffix.lower() == ".pdf":
        return p
        
    all_pdfs = list(root_dir.rglob("*.pdf"))
    for pdf in all_pdfs:
        if query.lower() in pdf.name.lower() or query.lower() in str(pdf).lower():
            return pdf
    return None

def main():
    parser = argparse.ArgumentParser(
        description="Chandamama Telugu AI Companion Notes Generator (8-Year-Old Grade 3 Edition)"
    )
    parser.add_argument(
        "--file",
        type=str,
        default=None,
        help="Process a single file of your choice (e.g. --file Chandamama-1947-8.pdf or full path)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process all ~700 files across all year folders in a loop"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List pending files without making any API calls"
    )
    parser.add_argument(
        "--max",
        type=int,
        default=None,
        help="Maximum number of books to process (e.g. --max 5)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing -AINotes.md files if they already exist"
    )
    args = parser.parse_args()

    client = get_client()

    # Case 1: Run for a single file of choice
    if args.file:
        target_pdf = find_matching_pdf(BASE_DIR, args.file)
        if not target_pdf:
            print(f"[ERROR] Could not find any PDF matching: '{args.file}' under {BASE_DIR}")
            sys.exit(1)
        process_book_chapter_by_chapter(client, target_pdf, force=args.force)
        return

    # Case 2: Batch run over all files
    all_pdfs = sorted(list(BASE_DIR.rglob("*.pdf")))
    total_books = len(all_pdfs)
    existing_notes = list(BASE_DIR.rglob("*-AINotes.md"))
    
    print(f"\n=======================================================")
    print(f"Total Chandamama Books: {total_books}")
    print(f"Existing Notes Files:   {len(existing_notes)}")
    print(f"Pending Books:          {total_books - len(existing_notes)}")
    print(f"=======================================================")
    print(f"Configured Models:      {' -> '.join(MODELS)}\n")

    if args.dry_run:
        print("[DRY RUN] Next pending files:")
        count = 0
        for pdf in all_pdfs:
            md_file = pdf.with_name(f"{pdf.stem}-AINotes.md")
            if not md_file.exists():
                print(f"  - {pdf.parent.name}/{pdf.name}")
                count += 1
                if count >= 15:
                    break
        return

    processed = 0
    for idx, pdf in enumerate(all_pdfs, start=1):
        md_file = pdf.with_name(f"{pdf.stem}-AINotes.md")
        if md_file.exists() and not args.force:
            continue

        print(f"\n>>> Starting Book [{idx}/{total_books}]: {pdf.parent.name}/{pdf.name}")
        success = process_book_chapter_by_chapter(client, pdf, force=args.force)
        if success:
            processed += 1

        if args.max and processed >= args.max:
            print(f"\nReached max limit of {args.max} books. Stopping.")
            break

if __name__ == "__main__":
    main()
