def calculate_power(base, exponent):
    """Calculates base^exponent using repeated multiplication (for positive integer exponents)."""
    if exponent == 0:
        return 1

    result = 1
    for _ in range(abs(exponent)):
        result *= base

    # If the original exponent was negative (handled by other exercises),
    # the reciprocal would be calculated later.
    if exponent>0:
        return result
    else:
        return 1/result

def nth_root_bisection(radicand, n, precision=0.000001, max_iterations=100):
    """
    Calculates the N-th root of a number using the Bisection Method.
    Includes logic for both precision (Ex 6) and max iterations (Ex 7).
    """
    if radicand == 0:
        return 0.0
    if n == 1:
        return radicand
    if radicand < 0 and n % 2 == 0:
        raise ValueError("Cannot compute even root of a negative number.")

    # Handle negative radicands (only possible for odd roots)
    if radicand < 0:
        return -nth_root_bisection(abs(radicand), n, precision, max_iterations)

    # 1. Establish initial bounds
    if radicand >= 1:
        low = 0.0
        high = float(radicand)
    else:  # For numbers between 0 and 1
        low = float(radicand)
        high = 1.0

    # 2. Iterate until desired precision or max iterations is met
    for i in range(max_iterations):
        mid = (low + high) / 2.0

        # Check termination condition for Ex 6 (precision)
        if (high - low) < precision:
            break

        mid_to_the_n = mid ** n  # Test the guess

        # 3. Adjust the bounds (Bisection)
        if mid_to_the_n > radicand:
            high = mid
        elif mid_to_the_n < radicand:
            low = mid
        else:
            return mid  # Exact match

    # Return the best approximation
    return (low + high) / 2.0

def prime_factorize(n):
    """Returns a dictionary of prime factors and their counts."""
    factors = {}
    d = 2
    temp = abs(n)

    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1

    return factors


# Exercise 12 Part B
def simplify_fraction(numerator, denominator):
    """
    Simplifies a fraction using prime factorization to find the GCD.
    Returns (simplified_numerator, simplified_denominator).
    """
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    if numerator == 0:
        return 0, 1

    num_factors = prime_factorize(numerator)
    den_factors = prime_factorize(denominator)

    common_divisor = 1

    # Iterate over prime factors of the numerator
    for prime, count_num in num_factors.items():
        if prime in den_factors:
            count_den = den_factors[prime]
            # The number of times this prime can be cancelled is the minimum count
            cancellation_count = min(count_num, count_den)
            common_divisor *= calculate_power(prime, cancellation_count)

    simplified_num = numerator // common_divisor
    simplified_den = denominator // common_divisor

    return simplified_num, simplified_den


# Exercise 12 Part C (Refined Power Calculation)
def calculate_non_integer_power_simplified(base, exponent_decimal, precision=0.000001):
    """
    The complete, efficient solution for fractional exponents:
    1. Converts decimal to fraction.
    2. Simplifies fraction using prime factorization.
    3. Computes the final power/root using Bisection.
    """
    is_negative = exponent_decimal < 0
    if is_negative:
        exponent_decimal = abs(exponent_decimal)

    # 1. Convert to improper fraction (p, q)
    p_raw, q_raw = decimal_to_fraction(exponent_decimal)

    # 2. Simplify fraction (p', q')
    p_prime, q_prime = simplify_fraction(p_raw, q_raw)

    print(f"--- Calculation for {base}^{exponent_decimal} ---")
    print(f"Fraction: {p_raw}/{q_raw} -> Simplified: {p_prime}/{q_prime}")

    # 3. Compute the result: (base^p')^(1/q')

    # Calculate Power (base^p')
    # Using built-in ** because p' can be very large
    power_result = base ** p_prime

    # Calculate Root (q'-th root of power_result)
    root_result = nth_root_bisection(power_result, q_prime, precision=precision)

    # Handle Negatives
    if is_negative:
        final_result = 1.0 / root_result
    else:
        final_result = root_result

    return final_result

def decimal_to_fraction(decimal_exponent):
    """
    Converts a decimal number to a raw improper fraction (numerator, denominator).
    Example: 5.2 -> (52, 10)
    """
    # Handle negative numbers
    sign = 1
    if decimal_exponent < 0:
        sign = -1
        decimal_exponent = abs(decimal_exponent)

    # Convert float to string to count decimal places
    s = str(decimal_exponent)
    if '.' not in s:
        # If it's an integer, like 5.0, treat it as 5/1
        return sign * int(decimal_exponent), 1

    # Get the number of digits after the decimal point
    decimal_places = len(s) - s.index('.') - 1

    # Denominator is 10 raised to the power of decimal places
    denominator = 10 ** decimal_places

    # Numerator is the entire number without the decimal point
    numerator = int(decimal_exponent * denominator)

    return sign * numerator, denominator

def prime_factorization(number):
    factors = {}
    d = 2
    temp = abs(number)

    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        temp += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors

print(prime_factorization(256)) # not working.

def simplify_a_fraction(numerator, denominator):
    if denominator == 0:
        raise ValueError(f"Denominator cannot be zero/0.")
    if numerator == 0:
        return 0, 1
    numerator_factors = prime_factorization(number = numerator)
    denominator_factors = prime_factorization(number = denominator)

    common_divisor = 1

    for prime, count_numerator in numerator_factors.items():
        if prime in denominator_factors:
            count_denominator = denominator_factors[prime]
            cancellation_count = min(count_numerator, count_denominator)
            common_divisor *= calculate_power(prime, cancellation_count)
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor

    return simplified_numerator, simplified_denominator

print(simplify_a_fraction(52, 10))

def calculate_non_integer_power_simplified(base, exponent_decimal, precision=0.000001):
    is_negative = exponent_decimal < 0
    if is_negative:
        exponent_decimal = abs(exponent_decimal)

    p_raw, q_raw = decimal_to_fraction(exponent_decimal)

    p_prime, q_prime = simplify_fraction(p_raw, q_raw)

    print(f"--- Calculation for {base}^{exponent_decimal} ---")
    print(f"Fraction: {p_raw}/{q_raw} -> Simplified: {p_prime}/{q_prime}")

    power_result = base ** p_prime

    root_result = nth_root_bisection(power_result, q_prime, precision=precision)
    if is_negative:
        final_result = 1.0 / root_result
    else:
        final_result = root_result
    return final_result

print(calculate_non_integer_power_simplified(100, 0.5))

print(calculate_non_integer_power_simplified(27, 0.6))
