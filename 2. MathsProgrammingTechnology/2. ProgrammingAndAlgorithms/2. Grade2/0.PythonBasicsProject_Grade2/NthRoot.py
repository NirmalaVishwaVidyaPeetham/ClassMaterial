# This function calculates the N-th root of a number (radicand)
# using the Bisection Method for high precision.
#
# Arguments:
#   radicand (float): The number whose root we want to find.
#   n (int): The index of the root (e.g., 2 for square root, 3 for cube root).
#   precision (float): How close we need to get to the true answer.
#
def nth_root_bisection(radicand, n, precision=0.000001):
    # Handle the simplest cases: root of 0, 1st root (n=1).
    if radicand == 0:
        return 0
    if n == 1:
        return radicand

    # 1. Establish the initial search bounds (low and high)
    # The root will always be between 0 and the radicand (if radicand > 1)
    # or between the radicand and 1 (if radicand < 1)
    if radicand >= 1:
        low = 0.0
        high = float(radicand)
    else:  # For numbers between 0 and 1
        low = float(radicand)
        high = 1.0

    # 2. Iteratively shrink the interval
    # The loop continues as long as the width of the interval (high - low)
    # is greater than the desired precision.
    while (high - low) > precision:
        # Find the midpoint of the current interval (our guess)
        mid = (low + high) / 2.0

        # Test the guess by raising it to the power of n
        mid_to_the_n = mid ** n

        # 3. Adjust the bounds (Bisection)
        if mid_to_the_n > radicand:
            # If our guess is too high, the true root must be in the lower half
            high = mid
        elif mid_to_the_n < radicand:
            # If our guess is too low, the true root must be in the upper half
            low = mid
        else:
            # Found the exact root (highly unlikely in floating point math)
            return mid

    # Once the loop ends, low and high are extremely close.
    # Return the average or either boundary as the accurate result.
    return (low + high) / 2.0


# --- Examples ---

# Example 1: Square Root of 25 (n=2)
result1 = nth_root_bisection(25, 2)
print(f"The square root of 25 is: {result1}")
# Should output 5.0

# Example 2: Cube Root of 10 (n=3) - as used in the lesson
result2 = nth_root_bisection(10, 3, precision=0.0001)
print(f"The cube root of 10 (4 decimal places) is: {result2}")
# Should output approx 2.1544

# Example 3: 5th Root of 32 (n=5)
result3 = nth_root_bisection(32, 5)
print(f"The 5th root of 32 is: {result3}")
# Should output 2.0

# "Negative n"th roots
result3 = nth_root_bisection(32, -5)