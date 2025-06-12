# we are writing this code without using list operations - append, remove

def sortedList(listOfNumbers):
    listSize = len(listOfNumbers);

    # This loop creates a sorted list from 0 to i after each iteration.
    for i in range(0,listSize):

        smallestIndex = i;
        # Find the smallest number from the index currentStartIndex/i to the end. Items before i are already sorted in the list
        for j in range(i+1,listSize):
            if listOfNumbers[smallestIndex] > listOfNumbers[j]:
                smallestIndex = j;
        # Now the smallest number from indices i to end is at j. So we swap j'th element with i'th element.
        #print(smallestIndex)
        temp = listOfNumbers[i]
        listOfNumbers[i] = listOfNumbers[smallestIndex];
        listOfNumbers[smallestIndex] = temp;
        print(listOfNumbers)
    return listOfNumbers

numbersList1 = [5.7,23.9,67.3,23.8,45.7]
sortedList(numbersList1)
numbersList2 = [5.7,23.9,67.3,23.8,67.3,45.7]
sortedList(numbersList2)
numbersList3 = [5.7,23.9, 23.8,67.3,23.8,67.3,45.7]
sortedList(numbersList3)