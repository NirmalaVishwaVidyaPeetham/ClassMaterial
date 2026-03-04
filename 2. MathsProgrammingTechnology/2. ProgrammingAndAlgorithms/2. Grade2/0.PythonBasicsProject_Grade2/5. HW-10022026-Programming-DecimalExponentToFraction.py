import math
def decimal_to_fractional_exponent(decimal_exponent):
    """
    This function converts a decimal exponent to a fractional exponent (Eg., 1.33 to 133/100)
    """
    numerator = decimal_exponent
    denominator = 1
    sign = 1
    if numerator < 0:
        sign = -1
        numerator = abs(numerator)

    #while not isinstance(numerator, int): # This doesn't work because of floating point error/precision etc.
    while not math.isclose(numerator, int(numerator),abs_tol=0.00000001):
        numerator = numerator*10;
        denominator = denominator*10;
        print(f"{numerator} {denominator}");

    return sign * int(numerator), denominator

print(decimal_to_fractional_exponent(decimal_exponent = 5.77))
print(decimal_to_fractional_exponent(decimal_exponent = 5.7777777777777))