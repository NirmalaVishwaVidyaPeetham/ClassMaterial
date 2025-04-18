# 1. Sum of Even Numbers:
def problem_1():
    sum = 0
    for i in range(2, 101, 2):
        sum = sum + i
        #print("sum=", sum, " ; i=")

    print(sum)


# 2. Multiplication Table:
def problem_2():
    for i in range(1, 11, 1):
        for j in range(11):
            print(i, 'x', j, '=', i * j)
        print()


# 3. Factorial Calculation:
def problem_3(number=5):

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


# 4. Prime Number Check:
def problem_4(number = 17):

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


# 5. Sum of Digits of a whole number:
def problem_5(number=1234):
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




#problem_1()
#problem_2()
#problem_3(6)
#problem_4(int(233482/2))
problem_5(-688.998)
problem_5(34567)
problem_5(688.998)
