# 1. Convert from Roman numerals to an integer:

def roman_to_int(roman_str):
    roman_numerals_dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    int_value = 0
    i = 0
    list1 = [roman_numerals_dictionary[roman_str[1]],...,]
    while i < len(roman_str):
        current_value = roman_numerals_dictionary[roman_str[i]]
        if i + 1 < len(roman_str):
            next_value = roman_numerals_dictionary[roman_str[i + 1]]
            if current_value < next_value:
                int_value += (next_value - current_value)
                i += 2
                continue
        int_value += current_value
        i += 1
    return int_value

print("-" * 50)

# 2. Convert from an integer to Roman numerals:

def int_to_roman(num):
    if num >= 1 and num <= 3999:
        roman_numeral = ""
        roman_map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        for value, symbol in roman_map:
            count = num // value
            roman_numeral += (symbol * count)
            num %= value
            if num == 0:
                break
    else:
        return "Number must be between 1 and 3999."
    return roman_numeral
print("-" * 50)

print(roman_to_int("MMCXXXCIVCD"))  # Invalid sequence
print(roman_to_int("CMXII"))
print(roman_to_int("LDCXIV"))       # Invalid sequence

print(int_to_roman(4893))
print(int_to_roman(0))
print(int_to_roman(32))

print(int_to_roman(476))
print(int_to_roman(559))