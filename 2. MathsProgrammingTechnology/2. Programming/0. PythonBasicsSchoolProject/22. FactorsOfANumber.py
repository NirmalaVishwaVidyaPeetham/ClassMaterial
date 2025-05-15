from math import sqrt
# To find factors of 'n', we only need to check from 1 to sqrt(n). If x**2 = n, then sqrt(n) = x
# Hint: Factors come inn pairs
def listOfFactors(n):
    if(not isinstance(n, int) or n<=0):
        print("Enter an integer >0")
        return
    listF = [1,n]
    for i in range(2,int(sqrt(n))):
        if n%i==0:
            listF.append(i)
            listF.append(int(n/i))
    print("List of factors of ", n, " = ", listF)
    return listF

# Getting the sorted list by separating the factors less than sqrt (which will be already sorted since we are going in loop from 1 to sqrt(n), and factors greater than sqrt, by reversing their order in appended list.
def listOfFactorsSorted(n):
    if(not isinstance(n, int) or n<=0):
        print("Enter an integer >0")
        return
    listFLower = [1]  # Values <= sqrt(n)
    listFHigher = [n] # Values > sqrt(n)

    for i in range(2,int(sqrt(n))):
        if n%i==0:
            listFLower.append(i)
            listFHigher = [int(n/i)] + listFHigher
    sortedList = listFLower + listFHigher
    print("List of factors of ", n, " = ", sortedList )
    return sortedList

listOfFactors(24)
listOfFactorsSorted(24)
listOfFactors(120)
listOfFactorsSorted(120)