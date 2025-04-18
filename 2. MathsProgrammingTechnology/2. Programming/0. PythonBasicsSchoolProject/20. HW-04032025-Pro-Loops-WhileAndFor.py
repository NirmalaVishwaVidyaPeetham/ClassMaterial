# 1. Sum of Even Numbers:
def problem_1_forLoop():
    sum = 0
    for i in range(2, 101, 2):
        sum = sum + i
        #print("sum=", sum, " ; i=", i)
    print("sum=", sum, " ; i=", i)
# while loop:
def problem_1_whileLoop():
    i = 2
    sum = 0
    while i <= 100:
        sum += i
        #print("sum=", sum, " ; i=", i)
        i = i + 2
    print("sum=", sum, " ; i=", i)
    # Compare the value of i at the end of while loop vs. for loop.

# 2. Multiplication Table:
def problem_2_forLoop():
    for i in range(1, 11, 1):
        print("Multiplication table for ", i)
        for j in range(11):
            print(i, 'x', j, '=', i * j)
        print()
def problem_2_whileLoop():
    i = 1
    while i<11 :
        print("Multiplication table for ", i)
        j = 0
        while j<11:
            print(i, 'x', j, '=', i * j)
            j += 1
        print()
        i+=1
def problem_2_whileAndForLoops():
    i = 1
    while i<11 :
        print("Multiplication table for ", i)
        j = 0
        for j in range(11):
            print(i, 'x', j, '=', i * j)
        print()
        i+=1

problem_1_forLoop()
problem_1_whileLoop()
problem_2_forLoop()
problem_2_whileLoop()
problem_2_whileAndForLoops()
