# AI Prompt: Using the description in canvas, write python code to convert roman numeral to decimal values and vice versa. Create a new canvas for the code.

"""
Roman Numeral Converter
This script provides two functions for converting between Roman numerals (up to 3999)
and standard decimal integers, based on the rules outlined in the provided documentation.
"""

def roman_to_int(s: str) -> int:
    """
    Converts a Roman numeral string to an integer.
    Uses the subtraction rule (e.g., IV = 4, CM = 900) by checking pairs of symbols.

    Args:
        s (str): The Roman numeral string (e.g., "MCMXCIV").

    Returns:
        int: The corresponding integer value (e.g., 1994).
    """
    # Define the mapping of symbols to values
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    integer_value = 0
    i = 0

    # Iterate through the Roman numeral string
    while i < len(s):
        # Get the value of the current symbol
        current_value = roman_map[s[i]]

        # Check if there is a next symbol
        if i + 1 < len(s):
            next_value = roman_map[s[i+1]]

            # Check for the subtraction rule (smaller value before larger value)
            # Examples: IV (4), IX (9), XL (40), XC (90), CD (400), CM (900)
            if current_value < next_value:
                # Subtractive pair found: Add the difference and skip the next symbol
                integer_value += (next_value - current_value)
                i += 2  # Move past both the current and the next symbol
                continue

        # If no subtraction is needed (addition rule applies)
        integer_value += current_value
        i += 1

    return integer_value

def int_to_roman(num: int) -> str:
    """
    Converts an integer (1 to 3999) to a Roman numeral string.
    Uses a greedy algorithm with predefined subtractive pairs for efficiency.

    Args:
        num (int): The integer value (e.g., 1994).

    Returns:
        str: The corresponding Roman numeral string (e.g., "MCMXCIV").
    """
    if not 1 <= num <= 3999:
        return "Error: Number must be between 1 and 3999."

    # Define the values and their corresponding Roman symbols,
    # including the subtractive pairs (CM, CD, XC, XL, IX, IV)
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
        (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
        (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    roman_numeral = ""

    # Iterate through the map from largest value to smallest
    for value, symbol in roman_map:
        # Check how many times the current value fits into the remaining number
        count = num // value

        # Append the symbol that many times to the result
        roman_numeral += (symbol * count)

        # Subtract the total amount added from the number
        num %= value

        # Stop if the number has been fully converted
        if num == 0:
            break

    return roman_numeral

# --- HOMEWORK PROBLEM SETS (200 Total) ---
# Combined Roman Numeral problems from Homework Set 1 and Set 2

roman_problems = [
    # Homework Set 1 (Problems 1-50)
    'XV', 'III', 'VIII', 'XI', 'XIV', 'XLI', 'LX', 'LXXXV', 'XCI', 'CD',
    'CM', 'CCXX', 'CCCLX', 'DLV', 'DCLX', 'DCCC', 'MXI', 'MCC', 'MCDL', 'MDLX',
    'MDCC', 'MCM', 'MMIV', 'MMDCC', 'MMCM', 'MMMCC', 'MMMCM', 'MMMCCCXL', 'MMMDCLX', 'MMMDCCXCIX',
    'MMMCMXC', 'XXII', 'LII', 'LXXIX', 'CXVII', 'CCXLIX', 'DCCLXII', 'CMXLIX', 'MMLIX', 'MMCMXCIX',
    'MMMCMXLVIII', 'XXXIX', 'CDXXIX', 'DCCLXXVII', 'MCCXXXIV', 'MDLXXX', 'CMXCI', 'MMCDLXIV', 'XXXVI', 'XIX',

    # Homework Set 2 (Problems 1-50)
    'VII', 'XLV', 'XCII', 'CXXIX', 'CDL', 'DCCIV', 'CMXL', 'MI', 'MCCCXXXIII', 'MDCCC',
    'MCMXLVI', 'MMXXXV', 'MMDCCXLIX', 'MMMDLXXXI', 'MMMCMXCIV', 'II', 'XVIII', 'LI', 'XCVII', 'CCXIII',
    'CCCLXIX', 'CDXC', 'DCCLXXXVIII', 'MVI', 'MCMLXXXIX', 'MMCDL', 'MMMDCCC', 'MMMCMIX', 'IV', 'IX',
    'XL', 'LIX', 'CCXL', 'CCCIV', 'CDXLIV', 'DXXVII', 'DCCL', 'MCCCLXVI', 'MMCXX', 'MMDCCCLXXXV',
    'MMMXC', 'MMMCCCXIX', 'MMMCDLXX', 'MMMCMXLI', 'LVIII', 'CCVI', 'DXXX', 'CMXCV', 'MDCXCV', 'MMCCCLV'
]

# Combined Integer problems from Homework Set 1 and Set 2

int_problems = [
    # Homework Set 1 (Problems 51-100)
    13, 27, 3, 4, 9, 18, 29, 40, 55, 83, 99, 104, 149, 200, 350, 400, 488, 512, 666, 799,
    845, 900, 999, 1001, 1250, 1400, 1575, 1660, 1800, 1999, 2024, 2333, 2444, 2500, 2789, 2900,
    2994, 3000, 3300, 3456, 3707, 3888, 3999, 17, 64, 110, 521, 1357, 2603, 30,

    # Homework Set 2 (Problems 51-100)
    2, 6, 19, 33, 49, 62, 78, 84, 109, 144, 187, 230, 315, 450, 509, 622, 707, 888, 940, 1050,
    1111, 1345, 1500, 1678, 1717, 1855, 1960, 2005, 2139, 2222, 2400, 2671, 2890, 3001, 3110, 3225,
    3330, 3404, 3588, 3600, 3749, 3801, 3900, 24, 50, 115, 560, 1090, 2550, 79
]

# --- EXECUTION AND HOMEWORK CHECK ---

print("=" * 60)
print("ROMAN TO DECIMAL CONVERSION CHECK (100 Problems)")
print("=" * 60)

for i, roman in enumerate(roman_problems):
    result = roman_to_int(roman)
    print(f"Problem {i+1:3}: {roman:<12} -> {result}")

print("\n" + "=" * 60)
print("DECIMAL TO ROMAN CONVERSION CHECK (100 Problems)")
print("=" * 60)

for i, num in enumerate(int_problems):
    result = int_to_roman(num)
    # The index here starts at 101 to correspond with the problem numbers in the homework sheets
    print(f"Problem {i+101:3}: {num:<4} -> {result}")

print("=" * 60)