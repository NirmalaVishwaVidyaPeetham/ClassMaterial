from math import sqrt
def listOfFactors(n):
    if(not isinstance(n, int) or n<=0):
        print("Enter an integer > 0")
        return
    i = 2
    listF = [1, n]
    while i <= int(sqrt(n)):
        if n%i==0:
            listF.append(i)
            listF.append(int(n/i))
        i += 1
    print("List of factors of", n, "(unsorted) = ", listF)
    return listF

# Getting the sorted list by separating the factors less than sqrt (which will be already sorted since we are going in loop from 1 to sqrt(n), and factors greater than sqrt, by reversing their order in appended list.
def listOfFactorsSorted(n):
    if(not isinstance(n, int) or n<=0):
        print("Enter an integer >0")
        return
    listFLower = [1]  # Values <= sqrt(n)
    listFHigher = [n] # Values > sqrt(n)
    i=2
    while i <= int(sqrt(n)):
        if n%i==0:
            listFLower.append(i)
            listFHigher = [int(n/i)] + listFHigher
        i += 1
    sortedList = listFLower + listFHigher
    print("List of factors of", n, "(sorted) = ", sortedList )
    return sortedList

listOfFactors(24)
listOfFactorsSorted(24)
listOfFactors(120)
listOfFactorsSorted(120)
listOfFactors(2520)
listOfFactorsSorted(2520)