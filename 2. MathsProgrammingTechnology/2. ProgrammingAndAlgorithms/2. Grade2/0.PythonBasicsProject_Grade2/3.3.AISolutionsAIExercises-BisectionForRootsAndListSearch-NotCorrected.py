import math


# --- Helper Function: Decimal to Fraction Conversion ---
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


# --- Section 1: Exponentials and Powers (Rules) ---

# Exercise 1
def calculate_power(base, exponent):
    """Calculates base^exponent using repeated multiplication (for positive integer exponents)."""
    if exponent == 0:
        return 1

    result = 1
    for _ in range(abs(exponent)):
        result *= base

    # If the original exponent was negative (handled by other exercises),
    # the reciprocal would be calculated later.
    return result


# Exercise 2
def check_product_rule(a, b, n):
    """Verifies the Power of a Product Rule: (a * b)^n = a^n * b^n"""
    if n < 0:
        # Simplification for non-integer exponents is complex; stick to integer n for verification
        return False

    left_side = calculate_power(a * b, n)
    right_side = calculate_power(a, n) * calculate_power(b, n)

    # Use math.isclose for floating point comparison tolerance
    return math.isclose(left_side, right_side)


# Exercise 3
def convert_negative_exponent(base, exponent):
    """Converts a negative exponent to its reciprocal string form."""
    if exponent >= 0:
        return f"{base}^{exponent}"

    positive_exponent = abs(exponent)
    return f"1 / {base}^{positive_exponent}"


# Exercise 4 (Simple Non-Integer Power Calculation) - Requires Ex 6 and Ex 1
def calculate_non_integer_power_simple(base, exponent_decimal):
    """
    Computes a^m using the fractional exponent rule and the Bisection Method.
    This version does NOT simplify the fraction first (unlike Ex 12).
    """
    is_negative = exponent_decimal < 0
    if is_negative:
        exponent_decimal = abs(exponent_decimal)

    p, q = decimal_to_fraction(exponent_decimal)  # p = numerator, q = denominator

    # Step 3: Calculate Power (a^p)
    # Note: Using Python's built-in ** here for simplicity and safety,
    # as p can be large, exceeding limits of the loop in Ex 1.
    power_result = base ** p

    # Step 4: Calculate Root (q-th root of a^p) - Requires Ex 6
    # Note: We use the implementation of nth_root_bisection defined below.
    root_result = nth_root_bisection(power_result, q)

    # Step 5: Handle Negatives
    if is_negative:
        return 1.0 / root_result

    return root_result


# --- Section 2: Roots and the Bisection Method ---

# Exercise 6 & 7 (Core Root Function)
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


# Exercise 5
def is_perfect_square_root(n, root):
    """Checks if 'root' is the integer square root of 'n'."""
    if root <= 0 or n <= 0:
        return False
    return root * root == n


# --- Section 3: Search Algorithms ---

# Exercise 8
def brute_force_search(data_list, target):
    """Implements Brute Force (Linear) search."""
    for index in range(len(data_list)):
        if data_list[index] == target:
            return index
    return -1


# Exercise 9
def binary_search_index(sorted_list, target):
    """Implements Binary Search on a sorted list."""
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Exercise 10 (Comparison)
def compare_search_speed(list_size, target):
    """
    Demonstration function for search speed comparison (simplified by counting steps
    in a dedicated function run, instead of modifying the core search functions).
    """
    import random

    # Generate sorted list
    data_list = sorted([random.randint(1, 1000000) for _ in range(list_size)])

    # To count steps, we need wrappers:
    def count_steps_linear(data, target):
        steps = 0
        for index in range(len(data)):
            steps += 1
            if data[index] == target:
                return steps, index
        return steps, -1

    def count_steps_binary(data, target):
        steps = 0
        low = 0
        high = len(data) - 1

        while low <= high:
            steps += 1
            mid = (low + high) // 2

            if data[mid] == target:
                return steps, mid
            elif data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return steps, -1

    bf_steps, bf_index = count_steps_linear(data_list, target)
    bs_steps, bs_index = count_steps_binary(data_list, target)

    print(f"\n--- Search Comparison (List Size: {list_size}) ---")
    print(f"Target: {target}")
    print(f"Brute Force (Index: {bf_index}): {bf_steps} steps")
    print(f"Binary Search (Index: {bs_index}): {bs_steps} steps")
    return bf_steps, bs_steps


# --- Section 4: Combination ---

# Exercise 11
def find_perfect_root(n):
    """
    Finds integer square or cube root of n using Binary Search principles.
    Uses an integer version of Bisection.
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return n

    # Find the integer root 'x' such that x^2 = n or x^3 = n
    low = 1
    high = n
    root_found = None

    while low <= high:
        mid = (low + high) // 2

        # Check for perfect square
        square = mid * mid
        if square == n:
            return mid  # Found perfect square root

        # Check for perfect cube
        cube = mid * mid * mid
        if cube == n:
            return mid  # Found perfect cube root

        if square > n:
            high = mid - 1
        else:
            low = mid + 1

    return None


# Exercise 12 Part A
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


# --- Demonstration and Testing ---

if __name__ == '__main__':
    print("==============================================")
    print("SECTION 1: POWERS")
    print("==============================================")

    # Ex 1 Test
    print(f"Ex 1: 3^4 = {calculate_power(3, 4)} (Should be 81)")

    # Ex 2 Test
    print(f"Ex 2: (2*5)^3 == 2^3 * 5^3: {check_product_rule(2, 5, 3)}")

    # Ex 3 Test
    print(f"Ex 3: 5^-3 converted: {convert_negative_exponent(5, -3)}")

    # Ex 4 Test (Simple fractional power calculation)
    # 8^1.5 = 8^(3/2) = sqrt(8^3) = sqrt(512) approx 22.627
    result_ex4 = calculate_non_integer_power_simple(8, 1.5)
    print(f"\nEx 4 Simple: 8^1.5 = {result_ex4:.5f} (Target: 22.62742)")

    print("\n==============================================")
    print("SECTION 2: ROOTS (Bisection Method)")
    print("==============================================")

    # Ex 6 & 7 Test (nth_root_bisection)
    # 5th root of 100,000 is 10
    root_result_ex6 = nth_root_bisection(100000, 5)
    print(f"Ex 6/7: 5th root of 100000 = {root_result_ex6:.6f} (Should be 10.0)")

    # Ex 5 Test
    print(f"Ex 5: Is 8 the square root of 64? {is_perfect_square_root(64, 8)}")
    print(f"Ex 5: Is 9 the square root of 80? {is_perfect_square_root(80, 9)}")

    print("\n==============================================")
    print("SECTION 3: SEARCH ALGORITHMS")
    print("==============================================")

    test_list = [5, 12, 18, 25, 33, 40]
    target = 33

    # Ex 8 Test
    print(f"Ex 8 (Brute Force): Index of 33 in {test_list}: {brute_force_search(test_list, target)}")

    # Ex 9 Test
    print(f"Ex 9 (Binary Search): Index of 33 in {test_list}: {binary_search_index(test_list, target)}")

    # Ex 10 Test
    compare_search_speed(10000, 500)
    compare_search_speed(10000, 9999999)  # Target likely not in the list

    print("\n==============================================")
    print("SECTION 4: COMBINATION")
    print("==============================================")

    # Ex 11 Test
    print(f"Ex 11: Perfect root of 100: {find_perfect_root(100)} (Should be 10)")
    print(f"Ex 11: Perfect root of 8: {find_perfect_root(8)} (Should be 2)")
    print(f"Ex 11: Perfect root of 11: {find_perfect_root(11)} (Should be None)")

    # Ex 12 Test (Prime Factorization and Simplification)
    num_raw, den_raw = 52, 10
    num_sim, den_sim = simplify_fraction(num_raw, den_raw)
    print(f"\nEx 12 Part A/B:")
    print(f"52/10 simplified: {num_sim}/{den_sim} (Should be 26/5)")

    # Ex 12 Test (Full Calculation)
    # Test 1: 4^(2.5) = 4^(5/2) = sqrt(4^5) = sqrt(1024) = 32
    base1, exponent1 = 4, 2.5
    result_ex12_1 = calculate_non_integer_power_simplified(base1, exponent1)
    print(f"\nEx 12 Part C: {base1}^{exponent1} = {result_ex12_1:.6f} (Target: 32.0)")

    # Test 2: 27^(-1/3) = 27^(-0.333...) = 1/3 = 0.333...
    base2, exponent2 = 27, -1 / 3
    result_ex12_2 = calculate_non_integer_power_simplified(base2, exponent2)
    print(f"Ex 12 Part C: {base2}^{exponent2} = {result_ex12_2:.6f} (Target: 0.333333)")