MAXNUM = 100
numbers = list( range(2,MAXNUM+1) )
i = 0
while i < len( numbers ):
    j = i+1
    while j < len( numbers ):
        if numbers[j]%numbers[i]:
            j += 1
        else:
            numbers.pop(j)
    i += 1
for i in numbers:
    print( i, end=" " )
