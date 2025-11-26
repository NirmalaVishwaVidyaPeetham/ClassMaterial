# --- 1. Bisection Method for N-th Root (Numerical) ---

def nth_root_bisection(radicand, n, precision=0.000001):
    """
    Calculates the N-th root of a number using the Bisection Method.
    This method works on a continuous number line (domain).
    """
    if radicand == 0:
        if n<0:
            raise ValueError("Root index 'n' cannot be negative if radicand is zero.")
        else:
            return 0
    if n == 0:
        raise ValueError("Root index 'n' cannot be zero.")

    # 1. Establish initial bounds
    low = 0.0
    high = float(radicand) if radicand >= 1 else 1.0
                # This is since x**4 < x if 0<x<1; If x>1, then x**4>x;

    # 2. Iterate until desired precision is met
    while (high - low) > precision:
        mid = (low + high) / 2.0

        # Check the midpoint value against the radicand
        if mid ** n > radicand:
            # Result is in the lower half
            high = mid
        else:
            # Result is in the upper half or equal
            low = mid

    return (low + high) / 2.0


# --- 2. Binary Search (Element Search) ---

def binary_search(data_list, target):
    """
    Searches for a target element in a sorted list using the Binary Search Method.
    This method works on a discrete, sorted set (domain).
    Returns the index if found, otherwise returns -1.
    """
    low = 0
    high = len(data_list) - 1

    if(data_list[low]<=target and data_list[high]>=target):
        while low <= high:
            # Find the middle index
            mid = (low + high) // 2  # Integer division as index has to be whole number

            # Test the value at the midpoint index
            if data_list[mid] == target:
                return mid  # Target found
            elif data_list[mid] < target:
                # Target is in the upper half (discard left)
                low = mid + 1
            else:
                # Target is in the lower half (discard right)
                high = mid - 1

    return -1  # Target not found


# --- 3. Brute Force Search (Linear Search) ---

def brute_force_search(data_list, target):
    """
    Searches for a target element by checking every item sequentially.
    (Also known as Linear Search)
    """
    for index in range(len(data_list)):
        if data_list[index] == target:
            return index  # Target found
    return -1  # Target not found


# --- Demonstration ---

print("--- Root Finding (Bisection Method) ---")
radicand = 100
n_root = 3
root_result = nth_root_bisection(radicand, n_root, precision=0.000001)
print(f"The {n_root}rd root of {radicand} is: {root_result:.6f}\n")

print("--- Element Search Comparison ---")
sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23

# Binary Search Test
bs_index = binary_search(sorted_list, target_value)
print(f"Binary Search: Target {target_value} found at index: {bs_index}")

# Brute Force Test
bf_index = brute_force_search(sorted_list, target_value)
print(f"Brute Force Search: Target {target_value} found at index: {bf_index}")

# Example of element not found
target_missing = 50
print(f"\nSearching for missing target {target_missing}:")
print(f"Binary Search result: {binary_search(sorted_list, target_missing)}")
print(f"Brute Force result: {brute_force_search(sorted_list, target_missing)}")

import numpy as np
import time

# Create a Generator object with a specific seed for reproducibility; This allows to generate the same random list when running the code again and again
rng = np.random.default_rng(seed=42)
# Generate a 1x10 array of random integers between 1 (inclusive) and 100 (exclusive)
random_array_2d = rng.integers(1, 10000000, size=10000000)
print(random_array_2d)
random_array_2d_sorted = np.sort(random_array_2d);
print(random_array_2d_sorted)
#random_array_2d_sorted = random_array_2d_sorted.tolist()
# Example of element not found
target = 50
print(f"\nSearching in a huge list for target {50}:")

start_time_binary_search = time.perf_counter()
print(f"Binary Search result: {binary_search(random_array_2d_sorted, target)}")
end_time_binary_search = time.perf_counter()
time_for_binary_search = end_time_binary_search - start_time_binary_search;

start_time_bruteforce_search = time.perf_counter()
print(f"Brute Force result: {brute_force_search(random_array_2d_sorted, target)}")
end_time_bruteforce_search = time.perf_counter()
time_for_bruteforce_search = end_time_bruteforce_search - start_time_bruteforce_search;

print("Time for binary vs brute force search vs bruteforce/binary: ", time_for_binary_search, time_for_bruteforce_search, time_for_bruteforce_search/time_for_binary_search)

print("Brute force took", time_for_bruteforce_search/time_for_binary_search, "times longer than binary search")