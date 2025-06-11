from math import sqrt
import time

# function prime numbers version 1.2
def prime(number):
    for i in range(2, number, 1):
        if number % i == 0:
#           print(number, 'is not prime')
            return False
#    print(number, 'is prime')
    return True


# version 2.1
def newPrime(number):
    for i in range(2, int(sqrt(number)+1)):
        if number % i == 0:
            #print(number, 'is not prime')
            return False
    return True

t = prime(7)
print(t)
t = prime(8)
print(t)
t = newPrime(number = 6)
print(t)
t = newPrime(number = 27)
print(t)

print()
print(prime(73)); print(newPrime(73))
print(prime(99)); print(newPrime(99))