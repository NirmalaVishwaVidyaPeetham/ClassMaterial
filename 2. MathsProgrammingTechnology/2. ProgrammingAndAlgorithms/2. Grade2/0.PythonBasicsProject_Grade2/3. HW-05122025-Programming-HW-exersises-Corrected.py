# Section 1: Exponentials and Powers (Rules):

# 1. Write a Python function calculate_power(base, exponent) that calculates the result of the base raised to a positive integer exponent without using Python's built-in ** operator, or math.pow(). Use a loop and the principles of repeated multiplication:
def calculate_power(base, exponent):
    # We are using only integer exponent; For decimal exponents like x^1.5 = x^(3/2), we need to compute the square root of x^3 using bisection method.
    if not isinstance(exponent, int):
        print("Exponent has to be an integer")
        return None
    if base == 0:
        if exponent > 0:
            return 0
        else:
            print("Exponent has to be greater than 0 for base 0")
            return None
    ans = 1
    for _ in range(abs(exponent)):
        ans *= base
    if exponent >= 0:
        return ans
    else:
        return 1/ans;
print(calculate_power(2, 10))
print(calculate_power(2, -2))
print(calculate_power(2, 0))
print(calculate_power(2, 1.7))


# 2.  Write a function check_product_rule(a, b, n) that verifies the Power of a Product Rule (a × b)**n = a**n × b**n by calculating both sides separately and returning True if they are equal (within a small tolerance for floating point numbers).

import math

def check_product_rule(a, b, n):
    x = (a * b) ** n
    y = a ** n * b ** n
    if x == y:
        return True
    else:
         return False
print(check_product_rule(3, 2, 3))

def check_product_rule_2(a, b, n):
    power_ab = 1
    ans_a = 1
    ans_b = 1
    for i1 in range(0, n, 1):
        power_ab *= a * b
    for i2 in range(0, n, 1):
        ans_a *= a
    for i3 in range(0, n, 1):
        ans_b *= b
    if power_ab == ans_a * ans_b:
        return True
    else:
        return False
print(check_product_rule_2(3, 2, 3))

def check_product_rule_ai(a, b, n):
    """Verifies the Power of a Product Rule: (a * b)^n = a^n * b^n"""
    if n < 0:
        # Simplification for non-integer exponents is complex; stick to integer n for verification
        return False

    left_side = calculate_power(a * b, n)
    right_side = calculate_power(a, n) * calculate_power(b, n)

    # Use math.isclose for floating point comparison tolerance
    return math.isclose(left_side, right_side)
print(check_product_rule_ai(3, 2, 3))



# 3. Write a function convert_negative_exponent(base, exponent) that takes a negative integer exponent and converts the expression to its reciprocal form. For example, if the input is (3, -2), the function should return the equivalent positive form as a string: "1 / 3^2".

def convert_negative_exponent(base, exponent):
    if exponent >= 0:
        return str(base) + "^" + str(exponent)
    else:
        return "1 / " + str(base) + "^" + str(-1 * exponent)
print(convert_negative_exponent(base = 3, exponent = -2))
print(convert_negative_exponent(base = 3, exponent = 2))

# Exercise 3
def convert_negative_exponent(base, exponent):
    """Converts a negative exponent to its reciprocal string form."""
    if exponent >= 0:
        return f"{base}^{exponent}"
        # Python f-strings (formatted string literals), introduced in Python 3.6, provide a concise and readable way to embed Python expressions inside string literals.
        # Basic Syntax
        # Prefix the string with the letter f (or F) and place expressions within curly braces {}
    positive_exponent = abs(exponent)
    return f"1 / {base}^{positive_exponent}"
print(convert_negative_exponent(base = 3, exponent = -2))
print(convert_negative_exponent(base = 3, exponent = 2))


# TODO: Note by Virata Pusuluri/Student: Exercise 6 was done before exercise 4 because exercise 4 uses exercise 6.

# 6. Recreate the nth_root_bisection(radicand, n, precision) function. This is the core task: implement the logic to find the n-th root by iteratively halving the search interval until the difference between the high and low bounds is less than the specified precision.

# Code not verified
def nth_root_bisection(radicand = 18, n = 4, precision = 0.0001):
    low = 0
    while (low + 1) ** n <= radicand:
        low += 1
    if low ** n == radicand:
        return low

    high = low + 1
    mid = (low + high) / 2
    while high - low >= precision:
        if mid ** n < radicand:
            low = mid
            mid = (low + high) / 2
        elif mid ** n > radicand:
            high = mid
            mid = (low + high) / 2
        else:
            return mid
#    print(low, high - low, high)
    return mid
print(nth_root_bisection(16, 4, 0.000001))
print(nth_root_bisection(14, 4, 0.000001))

# Exercise 6 & 7 (Core Root Function)
# Code not verified
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
print(nth_root_bisection(16, 4, 0.000001))
print(nth_root_bisection(14, 4, 0.000001))

# 4. This exercise requires you to compute a**m where m is a non-integer (e.g., 5.2 or -1.5). The solution must use the Bisection Method (from Exercise 6) for the root part of the calculation. Steps:
# 1. Fraction Conversion: Convert the floating-point exponent m into an improper fraction. Example: m = 5.2 becomes 52/10.
# 2. Apply Rule: Transform the calculation using the fractional exponent rule: a**p/q = q-th root of a**p.
# 3. Calculate Power: Compute the numerator's power, a**p. 4. Calculate Root: Use the Bisection Method ( nth_root_bisection from Exercise 6) to find the q-th root of the result from Step 3.
# 5. Handle Negatives: If the original exponent was negative, use the Negative Exponent Rule (Exercise 3) to take the reciprocal of the final result.
# Note: For the most efficient calculation, proceed to Exercise 12 to learn how to simplify the fraction first.


# Exercise 4 (Simple Non-Integer Power Calculation) - Requires Ex 6 and Ex 1
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

try:
    print(calculate_non_integer_power_simple(16,1.25))
    #Fails to compute as it doesn't simplify 125/100 = 5/4;
except:
    print("error: unable to compute large value");


# --- Section 2: Roots and the Bisection Method ---

# 5. Write a function is_perfect_square_root(n, root) that checks if a given integer root is the correct integer square root of n. Example: is_perfect_square_root(64, 8) should return True.

def is_perfect_square_root(n, root, abs_tol=0.5):
    # if root ** 2 == n:
    #     return True
    # else:
    #     return False

    # use the following to compare floating point values within a given tolerance
    return math.isclose(root**2, n, abs_tol=abs_tol)
print(is_perfect_square_root(64.1, 8))
print(is_perfect_square_root(64.1, 8, abs_tol=0.00001))

# 7. Modify the Bisection Method function from Exercise 6 to stop after a maximum number of iterations (e.g., 15) instead of based on precision. Return the current best approximation. This demonstrates the logarithmic speed of the algorithm.

# Not verified
def root_approximation(radicand, n, iterations):
    low = 0
    while (low + 1) ** n <= radicand:
        low += 1
    if low ** n == radicand:
        return low

    high = low + 1
    mid = (low + high) / 2
    for i in range(1, iterations + 1, 1):
        if mid ** n < radicand:
            low = mid
            mid = (low + high) / 2
        elif mid ** n > radicand:
            high = mid
            mid = (low + high) / 2
        else:
            return mid
#    print(low, high - low, high)
    return mid
import time
start = time.perf_counter()
root_approximation(27, 4, 15)
end = time.perf_counter()
print(end-start)
start1 = time.perf_counter()
root_approximation(100000037, 4, 15)
end1 = time.perf_counter()
print(end1-start1)
start2 = time.perf_counter()
root_approximation(27, 4, 30)
end2 = time.perf_counter()
print(end2-start2)


# --- Section 3: Search Algorithms ---

# 8. Write the Python function brute_force_search(data_list, target) that implements the Brute Force (Linear) search algorithm. It should return the index of the target if found, or -1 if it is not found. The list does not need to be sorted.

def brute_force_search(data_list, target):
    for i in range(0, len(data_list), 1):
        if data_list[i] == target:
            return i
    else:
        return -1
print(brute_force_search(data_list = [7, 2, 9, 100, 76, 11], target = 7))
print(brute_force_search(data_list = [6, 7, 12, 66, 37, 46, 17], target = 70))

# 9. Write the Python function binary_search_index(sorted_list, target) that implements the Binary Search algorithm. It must require that the input list is sorted and should return the index of the target or -1 if not found.
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
binary_search_index(sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], target = 3)


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
compare_search_speed(10000,25)

# --- Section 4: Combination ---

# Section 4: Combination

# 11. Write a function find_perfect_root(n) that uses Binary Search principles to efficiently find the integer root of an integer n.
#   If n is a perfect square (e.g., 100), return its root (10).
#   If n is a perfect cube (e.g., 27), return its root (3).
#   If n is neither, return None.

def find_perfect_root(n):
    # STEP 1: Input Validation
    # We check if 'n' is a positive integer.
    # Perfect powers (roots) are typically defined for positive integers in this context.
    if not isinstance(n,int) or n<=0:
        print("Enter a positive integer");
        return None

    # STEP 2: Initialize the exponent
    # We start searching with an exponent of 2 (checking for perfect squares).
    exponent = 2;

    # STEP 3: Outer Loop - Iterate through potential exponents
    # We only need to check exponents where 2^exponent is less than or equal to n.
    # If 2^exponent > n, no integer base >= 2 can satisfy the condition.
    while 2**exponent <= n:
        # STEP 4: Inner Loop - Search for the base
        # For the current exponent, we try to find an integer base such that base^exponent == n.
        base = 2;
        while True:
            # Calculate the value for the current base and exponent
            n_current = base ** exponent
            if n_current== n:
                # CASE A: We found a match!
                # Return the base and the exponent as a tuple.
                return base,exponent
            elif n_current < n:
                # CASE B: The result is still too small.
                # Increment the base to check the next integer.
                base += 1;
            else:
                # CASE C: The result has exceeded 'n'.
                # There is no integer base for this specific exponent that will equal 'n'.
                # Break the inner loop to try the next exponent.
                break;

        # Increment the exponent to check the next power (e.g., from square to cube)
        exponent +=1;

    # STEP 5: Final Return
    # If the loops finish without returning a match, 'n' is not a perfect power.
    return None;


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

#-----------Virata added this---------
print(prime_factorize(n = 100))
#-----------

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

simplify_fraction(125,100)
simplify_fraction(500,100)

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
    # power_result = base ** p_prime
        # If we use this built in function, we can directly give the decimal value itself - no need to do all of this; Instead we are trying to build our own function.
    power_result = calculate_power(base, p_prime)

    # Calculate Root (q'-th root of power_result)
    root_result = nth_root_bisection(power_result, q_prime, precision=precision)

    # Handle Negatives
    if is_negative:
        final_result = 1.0 / root_result
    else:
        final_result = root_result

    return final_result
print(calculate_non_integer_power_simplified(4,1.25))

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
        # The result is correct as -1/3 is not being passed as a fraction but as a decimal approximation
