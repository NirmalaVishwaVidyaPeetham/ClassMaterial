# Finding nth root of a number using a brute force method
# Upto a precision 0.0001
# Precision for x is not the same as precision for x**5
# If we want x**5 to be precise upto p decimals, then x should be precise for even more decimals than p because small change x will give a large change in x**5.
# For this code, we only care about the closest value of x up to 4 decimals so that x**5 is near desired value
def bruteForceNthroot(radicand, n, precision=0.0001):
    if (radicand<0 or n<=0):
        print("Enter positive values")
        return
    starting_number = 0
    while starting_number ** n < radicand:
        starting_number += 1

    if starting_number ** n == radicand:
        return starting_number

    starting_number -= 1
    print('starting number is', starting_number)

    # This code works because we are starting from an integer whose **n is <radicand, and then keep increasing the value until the difference change sign to negative from positive
    #while radicand - starting_number ** n > precision:
    while radicand - starting_number ** n >= 0:
        print("starting value: ",starting_number,"has precision", (radicand - starting_number ** n ))
        starting_number += precision
#        print('starting number is', starting_number)
    print("starting value: ", starting_number, "has precision", (radicand - starting_number ** n));
    print("Answer is: ", starting_number-precision);

    return starting_number-precision

print(bruteForceNthroot(33, 5))
print(bruteForceNthroot(32, 5))
print(bruteForceNthroot(-32, 5))
print(bruteForceNthroot(0, 5))