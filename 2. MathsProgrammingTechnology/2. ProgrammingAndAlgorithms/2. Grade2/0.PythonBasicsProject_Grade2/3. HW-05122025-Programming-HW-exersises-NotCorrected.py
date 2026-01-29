# Section 1: Exponentials and Powers (Rules):
# import math
# import random
# 1. Write a Python function calculate_power(base, exponent) that calculates the result of the base raised to a positive integer exponent without using Python's built-in ** operator, or math.pow(). Use a loop and the principles of repeated multiplication:

def calculate_power(base, exponent):
    ans = 1
    for i in range(exponent):
        ans *= base
    # to check: print(pow(base, exponent), ans)
    return ans
calculate_power(2, 10)

# 2.  Write a function check_product_rule(a, b, n) that verifies the Power of a Product Rule (a × b)**n = a**n × b**n by calculating both sides separately and returning True if they are equal (within a small tolerance for floating point numbers).

def check_product_rule(a, b, n):
    m = (a * b) ** n
    n = a ** n * b ** n
    if m == n:
        return True
    else:
         return False
check_product_rule(3, 2, 3)

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

# 3. Write a function convert_negative_exponent(base, exponent) that takes a negative integer exponent and converts the expression to its reciprocal form. For example, if the input is (3, -2), the function should return the equivalent positive form as a string: "1 / 3^2".

def convert_negative_exponent(base, exponent):
    if exponent >= 0:
        return str(base) + "^" + str(exponent)
    else:
        return "1 / " + str(base) + "^" + str(-1 * exponent)
print(convert_negative_exponent(base = 3, exponent = -2))

# 4. This exercise requires you to compute a**m where m is a non-integer (e.g., 5.2 or -1.5). The solution must use the Bisection Method (from Exercise 6) for the root part of the calculation. Steps:
# 1. Fraction Conversion: Convert the floating-point exponent m into an improper fraction. Example: m = 5.2 becomes 52/10.
# 2. Apply Rule: Transform the calculation using the fractional exponent rule: a**p/q = q-th root of a**p.
# 3. Calculate Power: Compute the numerator's power, a**p. 4. Calculate Root: Use the Bisection Method ( nth_root_bisection from Exercise 6) to find the q-th root of the result from Step 3.
# 5. Handle Negatives: If the original exponent was negative, use the Negative Exponent Rule (Exercise 3) to take the reciprocal of the final result.
# Note: For the most efficient calculation, proceed to Exercise 12 to learn how to simplify the fraction first.

# TODO: Note by Virata Pusuluri/Student: Exercise 6 was done before exercise 4 because exercise 4 uses exercise 6.

# 6. Recreate the nth_root_bisection(radicand, n, precision) function. This is the core task: implement the logic to find the n-th root by iteratively halving the search interval until the difference between the high and low bounds is less than the specified precision.

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

def floating_point_normal_or_non_integer_power_calculation(a, m):
    digits_after_decimal_point = 1 # TODO: I didn't know how to set this variable.
    q = 10 ** digits_after_decimal_point
    p = m * q
    a_power_p = a ** p
    root = nth_root_bisection(radicand = a_power_p, n = q)
    if m < 0:
        return 1 / root
    else:
        return root
floating_point_normal_or_non_integer_power_calculation(a = 2, m = 5.2)

# Section 2: Roots and the Bisection Method

# 5. Write a function is_perfect_square_root(n, root) that checks if a given integer root is the correct integer square root of n. Example: is_perfect_square_root(64, 8) should return True.

def is_perfect_square_root(n, root):
    if root ** 2 == n:
        return True
    else:
        return False
print(is_perfect_square_root(64, 8))

# 7. Modify the Bisection Method function from Exercise 6 to stop after a maximum number of iterations (e.g., 15) instead of based on precision. Return the current best approximation. This demonstrates the logarithmic speed of the algorithm.

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
print(root_approximation(27, 3, 15))

# Section 3: Search Algorithms

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

def binary_search_index(sorted_list: list, target: int):
    low = 0
    high = len(sorted_list) - 1
    mid = (low + high) // 2
    while low <= high:
        if target == sorted_list[mid]:
            return mid
        elif target < sorted_list[mid]:
            low = mid + 1
            mid = (low + high) // 2
        else:
            high = mid - 1
            mid = (low + high) // 2
    return -1
binary_search_index(sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], target = 3)

# 10. Write a function compare_search_speed(list_size, target) that generates a random, sorted list of a given list_size. The function should then run both brute_force_search and binary_search_index for a random target and report the number of comparisons each method took (you will need to modify the search functions to count steps).

def compare_search_speed(list_size: list, target: int):
    def binary_search_problem_10(sorted_list, target):
        comparision = 0
        low = 0
        high = 0
        mid = (low + high) // 2
        while low <= high:
            comparision += 1
            if target == sorted_list[mid]:
                comparision += 1
                return comparision
            elif target < sorted_list[mid]:
                low = mid + 1
                mid = (low + high) // 2
                comparision += 1
            else:
                high = mid - 1
                mid = (low + high) // 2 # TODO: Check: should I keep the statement, "comparision += 1" here also?
            return comparision
    def brute_force_search_problem_10(data_list, target):
        comparision = 0
        for i in range(0, len(data_list), 1):
            comparision += 1
            if data_list[i] == target:
                comparision += 1
        return comparision
    print(binary_search_problem_10(sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 7))
    print(brute_force_search_problem_10(data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 7))
print(compare_search_speed([11], 5))

# Section 4: Combination

# 11. Write a function find_perfect_root(n) that uses Binary Search principles to efficiently find the integer root of an integer n.
#   If n is a perfect square (e.g., 100), return its root (10).
#   If n is a perfect cube (e.g., 27), return its root (3).
#   If n is neither, return None.

def find_perfect_root_brute_force_while(n):
    to_check = 1
    while to_check ** 2 <= n or to_check ** 3 <= n:
        if to_check ** 2 == n or to_check ** 3 == n:
            return to_check
        to_check += 1
    return None

def find_perfect_root_brute_force_for(n):
    for i in range(1, n + 1, 1):
        if i ** 2 == n or i ** 3 == n:
            return i
    return None

def find_perfect_root_binary(n):
    list_to_search = [1,...,n]
    low = 0
    high = len(list_to_search) - 1
    mid = (low + high) // 2
    while low <= high:
        if int(mid) ** 2 == n or int(mid) ** 3 == n:
            return int(mid)
        elif int(mid) ** 2 == n or int(mid) ** 3 > n:
            high = mid
            mid = (low + high) // 2
        elif int(mid) ** 2 == n or int(mid) ** 3 < n:
            low = mid
            mid = (low + high) // 2
    else:
        return None

print(find_perfect_root_brute_force_while(26))
print(find_perfect_root_brute_force_for(26))
print(find_perfect_root_binary(26))

# TODO: I couldn't do Exercises 12A, 12B, and 12C. I couldn't understand those.
print(5^2)