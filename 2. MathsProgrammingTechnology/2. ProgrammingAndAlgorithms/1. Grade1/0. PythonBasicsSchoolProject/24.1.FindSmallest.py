def findSmallestNumberInList(listOfNumbers):
    smallest = listOfNumbers[1];   # this variable will have the smallest number in the list up to each iteration. When we complete 50 iterations, it will have the smallest of the first 50 items in the list.
    for i in listOfNumbers:
            # Think about what happens at the 51st iteration.
        if smallest > i:
            smallest = i;
        # else: # smallest is the smallest after 51 iterations
    # After checking that the loop code works for some iteration in the middle of the loop (51stt), check for the beginning and at the end.
    return smallest

print(findSmallestNumberInList([5,23,67,23,45]))
print(findSmallestNumberInList([5.7,23.9,67.3,23.8,45.7]))