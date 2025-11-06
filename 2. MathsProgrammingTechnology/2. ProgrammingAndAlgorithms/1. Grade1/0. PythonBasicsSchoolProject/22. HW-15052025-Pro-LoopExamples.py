# 7. Fibonachhi seqence: program that uses a for loop to generate the first 'n' numbers of the Fibonacci sequence (e.g., 0, 1, 1, 2, 3, 5, 8...).
def fibonachhi_seqence(number):
    i = 2
    mylist = [0, 1]
    while i <= number:
        value = mylist[i-1]+mylist[i-2]
        mylist.append(value)
        i=i+1
    #print(mylist)
    print(mylist[0:number])  # Doing this so if number is <2, it'll still work
    return
fibonachhi_seqence(1)
fibonachhi_seqence(5)
fibonachhi_seqence(10)

# 10. nested loops - print the following pattern:
# 1
# 1, 3
# 1, 3, 5 ...
def nested_loops(highest_number):
    for i in range(1, highest_number+1):
        if i%2 == 0:
            print()
            #continue
        else:
            for j in range(1, i+1, 2):
                print(j, end=" ") # end paraeter can be used to specity the last character after print. Default is '\n'
    print('\n')
# how to print in one line?
nested_loops(9)
nested_loops(12)
