from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, lightgrey, Color
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import sys
import time  # Added for timing progress

# --- IMPORTANT CONFIGURATION ---
# ⚠️ PREREQUISITE: You must have ReportLab installed (`pip install reportlab`).

# --- FONT HANDLING ---
# For non-Latin languages (Hindi, Telugu), you MUST use a font that supports those scripts.
# The default path is relative, but it's safer to point to an absolute path or a known system font.

# Try to find a font that supports multilingual text on common OSes:
FONT_NAME = "MultiLangFont"
FONT_PATH = "NotoSans-Regular.ttf"  # Default fallback, assumes font file is next to the script

# Attempt to locate a system font that typically supports Devanagari/Telugu:
if sys.platform.startswith('win'):
    # Common path for fonts on Windows
    font_folder = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')

    # FIX: Priority 1: Check for Noto Sans Telugu (Dedicated Telugu support)
    system_font_path_telugu = os.path.join(font_folder, "NotoSansTelugu-Regular.ttf")

    # Also check the common shortened filename
    if not os.path.exists(system_font_path_telugu):
        system_font_path_telugu = os.path.join(font_folder, "NotoSansTelugu.ttf")

    if os.path.exists(system_font_path_telugu):
        FONT_PATH = system_font_path_telugu
        FONT_NAME = "NotoTelugu"
        print("Note: Using NotoTelugu, prioritized for reliable Telugu rendering.")

    # Priority 2: Check for Nirmala UI (Known good for Hindi/English)
    elif os.path.exists(os.path.join(font_folder, "NIRMALA.TTF")):
        FONT_PATH = os.path.join(font_folder, "NIRMALA.TTF")
        FONT_NAME = "NirmalaUI"
        print("Note: Using NirmalaUI, prioritized for Hindi/English support. Telugu support may be limited.")

    elif os.path.exists(os.path.join(font_folder, "NIRMALAUI.TTF")):
        FONT_PATH = os.path.join(font_folder, "NIRMALAUI.TTF")
        FONT_NAME = "NirmalaUI"
        print("Note: Using NirmalaUI, prioritized for Hindi/English support. Telugu support may be limited.")

    # Priority 3: Check for Gautami (Older Telugu font)
    else:
        system_font_path_gautami = os.path.join(font_folder, "GAUTAMI.TTF")
        if os.path.exists(system_font_path_gautami):
            FONT_PATH = system_font_path_gautami
            FONT_NAME = "Gautami"
            print("Note: Using Gautami font (fallback). If Hindi fails, please check your system fonts.")

    # Final advice for the user
    if FONT_NAME != "NotoTelugu":
        print(
            "Action Required: For reliable Telugu rendering, please download 'NotoSansTelugu-Regular.ttf' and ensure it is installed in your Windows Fonts folder.")

elif sys.platform.startswith('linux'):
    # Common path for Noto Sans CJK on Linux systems
    system_font_path = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
    if os.path.exists(system_font_path):
        FONT_PATH = system_font_path
        FONT_NAME = "NotoSansCJK"
elif sys.platform == 'darwin':
    # Common path for a system font on macOS
    system_font_path = "/System/Library/Fonts/Supplemental/Devanagari Sangam MN.ttc"
    if os.path.exists(system_font_path):
        FONT_PATH = system_font_path
        FONT_NAME = "DevanagariSangam"

# --- Line Rule Dimensions (Parameterized 4-Line System - Relative Gaps) ---
# All Y positions are calculated based on these gaps, measured down the page.
# --------------------------------------------------------------------------------
# HOW TO ADJUST GAPS:
# RULE_OFFSET_TOP_LINE: The initial offset from the very top of the block.
# GAP_TOP_TO_MID: Distance between the Top Line (1) and Mid Line (2).
# GAP_MID_TO_BASE: Distance between the Mid Line (2) and Base Line (3).
# GAP_BASE_TO_DESC: Distance between the Base Line (3) and Descender Line (4).
# --------------------------------------------------------------------------------
RULE_OFFSET_TOP_LINE = 5  # Offset of Line 1 from the block top (was 5)

GAP_TOP_TO_MID = 13  # Gap between Line 1 (Capitals) and Line 2 (x-height)
GAP_MID_TO_BASE = 22  # Gap between Line 2 (x-height) and Line 3 (Baseline)
GAP_BASE_TO_DESC = 15  # Gap between Line 3 (Baseline) and Line 4 (Descenders)

# Initial space added before the very first line block
TOP_SPACING_ADJUSTMENT = 25

# Calculate the total height required for the rule area based on the gaps
RULE_AREA_HEIGHT = RULE_OFFSET_TOP_LINE + GAP_TOP_TO_MID + GAP_MID_TO_BASE + GAP_BASE_TO_DESC + 5
LINE_BLOCK_HEIGHT = RULE_AREA_HEIGHT + 15  # Total block height including vertical spacing

# Colors
RULE_COLOR = Color(0.6, 0.6, 0.6)  # Unused general rule color, kept for safety

# --- Line Specific Colors ---
COLOR_TOP_LINE = Color(0.1, 0.1, 0.6)  # Dark Blue (Cap Height/Ascenders)
COLOR_MID_LINE = Color(0.6, 0.1, 0.1)  # Dark Red (X-Height/Main Body)
COLOR_BASE_LINE = black  # Black (Baseline/Text Rest Point - Thickest Line)
COLOR_DESC_LINE = Color(0.1, 0.5, 0.1)  # Dark Green (Descender Limit)

TRACE_COLOR = Color(0, 0, 0, alpha=0.3)  # Transparent black for tracing text


# --- Core Function ---

def create_writing_practice_pdf(
        input_text,
        output_filename="writing_practice.pdf",
        num_tracing_lines=3,
        num_empty_lines=3,
        font_size=32
):
    """
    Generates a multi-page PDF for children's writing practice with ruled lines.
    """
    start_time = time.time()
    print(f"\n--- Starting PDF Generation for: {input_text} ---")

    # 1. Check and Register Font
    print(f"[{time.time() - start_time:.2f}s] Checkpoint 1: Verifying font file path...")
    if not os.path.exists(FONT_PATH):
        print(f"ERROR: Font file not found at {FONT_PATH}. Cannot generate multilingual text.")
        print(
            "Please check the FONT_PATH variable and update it with the full path to a suitable .ttf or .ttc file on your system (e.g., NotoSansTelugu-Regular.ttf).")
        return

    try:
        print(
            f"[{time.time() - start_time:.2f}s] Checkpoint 2: Attempting to register font '{FONT_NAME}' from: {FONT_PATH}")
        # FIX: Check if the file is a TrueType Collection (.ttc) and provide index=0.
        if FONT_PATH.lower().endswith('.ttc'):
            pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH, index=0))
        else:
            # For standard TTF/OTF files
            pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))
        print(f"[{time.time() - start_time:.2f}s] Checkpoint 3: Font registration SUCCESS.")

    except Exception as e:
        print(f"[{time.time() - start_time:.2f}s] ERROR: Font registration FAILED: {e}")
        return

    # 2. Setup the PDF canvas
    print(f"[{time.time() - start_time:.2f}s] Checkpoint 4: Setting up PDF canvas.")
    c = canvas.Canvas(output_filename, pagesize=A4)
    width, height = A4

    # Margins and starting position
    LEFT_MARGIN = 50
    RIGHT_MARGIN = width - 50
    TOP_START = height - 50

    # Apply initial vertical spacing here
    current_y = TOP_START - TOP_SPACING_ADJUSTMENT

    # Use the registered font name
    c.setFont(FONT_NAME, font_size)

    # 3. Helper function to draw the four ruled lines
    def draw_ruled_line(y_pos):
        """Draws the four-rule line system at a given Y position (top of the block)."""

        # Calculate absolute Y positions by accumulating the gaps
        # These coordinates (y_..._abs) are the fixed height lines relative to the bottom of the page.
        y_top_abs = y_pos + RULE_OFFSET_TOP_LINE
        y_mid_abs = y_top_abs + GAP_TOP_TO_MID
        y_base_abs = y_mid_abs + GAP_MID_TO_BASE
        y_descender_abs = y_base_abs + GAP_BASE_TO_DESC

        # Line 1: Main Baseline (Thick/Solid) - The line the text sits on
        # Drawn first as the most prominent reference line.
        c.setStrokeColor(COLOR_BASE_LINE)  # Color: Black (Thickest line)
        c.setLineWidth(1.5)
        c.setDash([])
        c.line(LEFT_MARGIN, y_base_abs, RIGHT_MARGIN, y_base_abs)

        # Line 2: Top Line (Thin/Solid) - Height of ascenders/capitals
        c.setStrokeColor(COLOR_TOP_LINE)  # Color: Dark Blue
        c.setLineWidth(0.5)
        c.line(LEFT_MARGIN, y_top_abs, RIGHT_MARGIN, y_top_abs)

        # Line 3: Mid-Line (Dotted) - Height of x-height letters
        c.setStrokeColor(COLOR_MID_LINE)  # Color: Dark Red
        c.setDash(2, 3)  # Set dash pattern
        c.setLineWidth(0.5)
        c.line(LEFT_MARGIN, y_mid_abs, RIGHT_MARGIN, y_mid_abs)

        # Line 4: Descender Line (Thin Dotted) - Lowest point for descenders
        c.setStrokeColor(COLOR_DESC_LINE)  # Color: Dark Green
        c.line(LEFT_MARGIN, y_descender_abs, RIGHT_MARGIN, y_descender_abs)

        # Reset dash and line width
        c.setDash()
        c.setLineWidth(1)

        # Return the absolute Y position of the baseline for text placement reference
        return y_base_abs

        # 4. Helper function to check for new page

    def check_new_page(y_pos):
        """Checks if a new page is needed and adds one if necessary."""
        # If the *next* line block's top edge (y_pos - LINE_BLOCK_HEIGHT) is below the bottom margin (50 points from bottom)
        if y_pos - LINE_BLOCK_HEIGHT < 50:
            c.showPage()
            c.setFont(FONT_NAME, font_size)  # Reapply font
            # Reset Y position to the top, minus the initial spacing
            return TOP_START - TOP_SPACING_ADJUSTMENT
        return y_pos

    # 5. Content Generation Loop
    print(f"[{time.time() - start_time:.2f}s] Checkpoint 5: Starting content generation loop.")

    # --- Initial Reference Text Block (Solid Black Color) ---
    current_y = check_new_page(current_y)
    y_base_for_text = draw_ruled_line(current_y)  # Get the baseline for text positioning

    # Draw the solid reference text
    c.setFillColor(black)
    # Positioning the text using the calculated baseline
    c.drawString(LEFT_MARGIN, y_base_for_text - (font_size * 0.25), input_text)

    # Move DOWN the page
    current_y -= LINE_BLOCK_HEIGHT

    # --- B. Main loop to fill pages with practice blocks ---
    page_count = 1
    # We subtract 1 from num_tracing_lines because the first one was already drawn as a solid reference
    remaining_tracing_lines = num_tracing_lines - 1 if num_tracing_lines > 0 else 0

    # Loop as long as we have space on the page (current_y > 50 points from bottom)
    while current_y > 50:

        # Check for new page BEFORE drawing the next block
        new_y = check_new_page(current_y)
        if new_y > current_y:  # Simple check: if Y increased, we reset to the top of a new page
            current_y = new_y
            page_count += 1
            print(f"[{time.time() - start_time:.2f}s] Checkpoint 5.1: New Page ({page_count}) started.")

        # --- 1. Tracing Lines (Transparent Text) ---
        for i in range(remaining_tracing_lines):
            y_base_for_text = draw_ruled_line(current_y)

            # Draw the transparent text for tracing
            c.setFillColor(TRACE_COLOR)
            # Adjust position to align with BASE_LINE
            c.drawString(LEFT_MARGIN, y_base_for_text - (font_size * 0.25), input_text)

            # Move DOWN the page
            current_y -= LINE_BLOCK_HEIGHT

        remaining_tracing_lines = num_tracing_lines  # Reset for subsequent pages

        # --- 2. Empty Lines (Free Writing) ---
        for i in range(num_empty_lines):
            draw_ruled_line(current_y)

            # Move DOWN the page
            current_y -= LINE_BLOCK_HEIGHT

        # Add space before repeating the set
        # Move DOWN the page
        current_y -= 20

        # Safety break condition
        if page_count > 10:
            print(f"Stopping execution after generating {page_count} pages for safety.")
            break

    # 6. Finalize the PDF
    print(f"[{time.time() - start_time:.2f}s] Checkpoint 6: Finalizing and saving PDF.")
    c.save()
    total_time = time.time() - start_time
    print(f"\n--- SUCCESS: PDF generated in {total_time:.2f} seconds: {output_filename} ---")


# --- Example Usage ---
# Added initial prints to show which font path the script decided to use.
print(f"** Script Configuration **")
print(f"System Detected: {sys.platform}")
print(f"Font Name Chosen: {FONT_NAME}")
print(f"Font Path Chosen: {FONT_PATH}")
print(f"Font Path Exists: {os.path.exists(FONT_PATH)}")

# Use the function call to generate the PDF when running the script:
create_writing_practice_pdf(
    input_text="मेरा नाम My name కృష్ణ కర్తవ్యం",
    output_filename="3. HandwritingCopyTracing_Output_Hindi.pdf",
    num_tracing_lines=5,  # This now means 1 solid reference line + 3 transparent tracing lines
    num_empty_lines=5,
    font_size=40
)