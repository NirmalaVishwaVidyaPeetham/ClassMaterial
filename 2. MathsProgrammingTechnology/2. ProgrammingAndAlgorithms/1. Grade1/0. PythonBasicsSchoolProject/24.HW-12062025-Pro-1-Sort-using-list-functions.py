# we are writing this code using list operations - append, remove, etc.
def smallest_number(A_List):
    smallest = A_List[0]
    # for i in range(0, len(A_List)):
    #     if smallest > A_List[i]:
    #         smallest = A_List[i]
    for a in A_List:
        if smallest > a:
            smallest = a;
    return smallest
def returnSortedList(ListOfNumbers):
    newList = []
    if len(ListOfNumbers) == 0:
        print('There has to be minimum 1 number in the list')
    while len(ListOfNumbers) > 0:
        s = smallest_number(ListOfNumbers)
        newList.append(s)
        ListOfNumbers.remove(s)
    return newList

numberList1 = [5, 8, 3, 66, 55]
print(smallest_number(numberList1))
numberList1 = [5, 8, 3, 66, 55, 8, 3]
print(smallest_number(numberList1))
numbersList1 = [5.7,23.9,67.3,23.8,45.7]
print(returnSortedList(numbersList1))
numbersList2 = [5.7,23.9,67.3,23.8,67.3,45.7]
print(returnSortedList(numbersList2))
numbersList3 = [5.7,23.9, 23.8,67.3,23.8,67.3,45.7]
print(returnSortedList(numbersList3))
