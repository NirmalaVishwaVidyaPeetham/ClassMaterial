# Write a python code to find the  GCD of 2 numbers
def GCF(x, y):
    if not(isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0):
        print('Give two integers >= 0')
        return
    if x == 0 and y == 0:
        print('Both numbers can\'t be zero')
        return
    if x == 0 and y > 0:
        GCD = y
        print('The GCD of', x, 'and', y, 'is', GCD)
    elif x > 0 and y == 0:
        GCD = x
        print('The GCD of', x, 'and', y, 'is', GCD)
    else:
        dividend = y ; divisor = x
        remainder = dividend % divisor
        while remainder != 0:
            dividend = divisor
            divisor = remainder
            remainder = dividend % divisor
        GCD = divisor
    return GCD

GCD = GCF(0,0)
print(GCD)

GCD = GCF(80,56)
print(GCD)