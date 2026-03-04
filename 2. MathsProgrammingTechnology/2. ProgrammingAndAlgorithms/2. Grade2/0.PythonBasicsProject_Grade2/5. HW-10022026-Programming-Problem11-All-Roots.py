# This function finds all the integer roots of a given integer n.
def find_all_possible_perfect_integer_roots(n):
    if not(isinstance(n, int) or n <= 0):
        print(f"Enter a positive integer.")
    roots_list = []
    exponent = 2
    while 2 ** exponent <= n:
        base = 2
        while True:
            n_current = base ** exponent
            if n_current == n:
                roots_list.append((f"{base} ** {exponent}"))
                break
            elif n_current < n:
                base += 1
                continue
            else:
                break
        exponent += 1
    if len(roots_list) == 0:
        return None
    else:
        return roots_list


def find_perfect_root_changed(n):
    # STEP 1: Input Validation
    # We check if 'n' is a positive integer.
    # Perfect powers (roots) are typically defined for positive integers in this context.
    if not isinstance(n,int) or n<=0:
        print("Enter a positive integer");
        return None
    Roots_list = []

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
                Roots_list.append((base, exponent))
                break
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
    return Roots_list if len(Roots_list) >= 1 else None

print(find_all_possible_perfect_integer_roots(n = 625))
print(find_all_possible_perfect_integer_roots(n = 81))
print(find_all_possible_perfect_integer_roots(n = 1024))
print(find_all_possible_perfect_integer_roots(n = (2**24)*(3**24)))

# Sir code changed
print(find_perfect_root_changed(n = 625))
print(find_perfect_root_changed(n = 81))
print(find_perfect_root_changed(n = 1024))
print(find_perfect_root_changed(n = 1024))
print(find_perfect_root_changed(n = (2**24)*(3**24)))