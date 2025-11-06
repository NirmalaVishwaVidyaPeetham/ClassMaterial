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


# 3. Factorial Calculation:
def problem_3_while_loop(number=5):

    number_factorial = 1

    # Using for loops
    # for i in range(1,number+1,1):
    #     number_factorial = number_factorial*i;

    # Using while loops
    i = 1;
    while i<=number:
        number_factorial = number_factorial * i
        i=i+1

    print(number, '\'s factorial is', number_factorial)
    return

def problem_3_for_loop(number):

    # using for
    number_factorial = 1
    for i in range(1, number + 1, 1):
        number_factorial = number_factorial * i;
    print(number, '\'s factorial is', number_factorial)

    return

def problem_4_for_loop(number = 17):
    if(not isinstance(number,int) or number<0):
        print("Number should be an integer >= 0 ")
        return
    isNumberPrime = True;
    firstDivisorGreaterThan1 = number;
    for i in range(2, number, 1):
        if number%i ==0:
            isNumberPrime = False;
            firstDivisorGreaterThan1 = i;
            break;
    if isNumberPrime:
        print(number,"is prime");
    else:
        print(number, "is not prime as it is divisible by ", firstDivisorGreaterThan1);
    return

def problem_4_while_loop(number):
    if(not isinstance(number,int) or number<0):
        print("Number should be an integer >= 0 ")
        return;
    isNumberPrime = True; firstDivisorGreaterThan1 = number;
    i = 2
    while i < number:
        if number%i ==0:
            isNumberPrime = False;
            firstDivisorGreaterThan1 = i;
            break;
        i = i + 1
    if isNumberPrime:
        print(number,"is prime");
    else:
        print(number, "is not prime as it is divisible by ", firstDivisorGreaterThan1);
    return



# 5. Sum of Digits of a whole number:
def problem_5_while_loop(number=1234):
    if(not isinstance(number,int) or number<0):
        print("Number should be an integer >= 0 ")
        return;
    sum = 0;
    currentNumber = number;
    while currentNumber>0:
        currentLastDigit = currentNumber%10;
        sum = sum + currentLastDigit;
        currentNumber = currentNumber//10;

    print("Sum of digits of ", number, " = ", sum);
    return

# See AI Notes on Loop conversion for more details on how to convert problem 5 from while to for loop.
def problem_5_for_loop(number=1234):
    if not isinstance(number, int) or number < 0:
        print("Number should be an integer >= 0")
        return

    sum_of_digits = 0
    number_str = str(number)  # Convert the number to a string

    for digit_char in number_str:
        digit = int(digit_char)  # Convert each character back to an integer
        sum_of_digits += digit

    print("Sum of digits of ", number, " = ", sum_of_digits)
    return

problem_1_forLoop()
problem_1_whileLoop()
problem_2_forLoop()
problem_2_whileLoop()
problem_2_whileAndForLoops()

problem_3_while_loop(4)
problem_3_for_loop(4)

problem_4_for_loop(int(233482/2))
problem_4_for_loop(233482)

problem_4_while_loop(int(233482/2))
problem_4_while_loop(233482)

problem_5_while_loop(324125145)
problem_5_for_loop(324125145)
