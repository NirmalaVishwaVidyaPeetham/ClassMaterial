### Function takes two parameters term1 and term2, adds them and returns their sum. It also verifies the result and prints results
def additionWithVerification(term1, term2):
    sum = term1 + term2
    print('Result of addition', term1, '+', term2, ' = ', sum)
    checkResult1 = (sum - term2 == term1)
    ## checkResult is a boolean variable of boolean data type
    print('Verification result1:', sum,'-',term2,'==',term1,' is ', checkResult1)
    checkResult2 = (sum - term1 == term2)
    print('Verification result2:', sum,'-',term1,'==',term2,' is ', checkResult2)
    checkWrongResult = (sum - term1 + 1 != term2)
    print('Wrong verification result:',sum,'-',term1,'+1 !=',term2,' is ', checkWrongResult, '\n')
    return sum

### Function takes two parameters minuend and subtrahend, subtracts and returns the difference. It also verifies the result and prints results
def subtractionWithVerification(minuend, subtrahend):
    difference = minuend-subtrahend
    print('Result of subtraction', minuend, '-', subtrahend, ' = ', difference)

    checkResult1 = (difference+subtrahend == minuend)
    print('Verification result1:', difference,'+',subtrahend,'==',minuend,' is ', checkResult1)

    checkWrongResult = (difference+subtrahend+1 != minuend)
    print('Wrong verification result:',difference,'+',subtrahend,'+1 !=',minuend,' is ', checkWrongResult, '\n')
    return difference

### Function takes two parameters multiplicand and multiplier, multiplies and returns their product. It also verifies the result and prints results
def multiplicationWithVerification(multiplicand, multiplier):
    product = multiplicand*multiplier
    print('Result of multiplication ',multiplicand, '*', multiplier, ' = ',  product)
    checkResult1 = (product/multiplicand == multiplier)
            ## checkResult is a boolean variable of boolean data type
    print('Verification result1:', product,'/',multiplicand,'==',multiplier,' is ', checkResult1)
    checkResult2 = (product/multiplier == multiplicand)
    print('Verification result2:', product,'/',multiplier,'==',multiplicand,' is ', checkResult2)
    checkWrongResult = (product/multiplicand+1 != multiplier)
    print('Wrong verification result:',product,'/',multiplicand,'+1 !=',multiplier,' is ', checkWrongResult, '\n')

def integerDivisionWithVerification(dividend, divisor):
    remainder = dividend % divisor
    quotient = dividend // divisor
    print('result of division : quotient ', dividend, '/', divisor, '=',quotient)
    print('result of division : remainder ',dividend, '%', divisor, '=' ,remainder)

    checkResult = (quotient * divisor + remainder == dividend)
    print('Verification result is ',quotient, '*' ,divisor,'+', remainder, '==' ,dividend, 'is' ,checkResult)
    checkWrongResult = (quotient * divisor + remainder + 1 != dividend)
    print('Wrong verification result is ',quotient,'*' ,divisor, '+', remainder,'+1','!=','is',dividend, 'is', checkWrongResult)

    return quotient, remainder

x = additionWithVerification(9846, 807)
x = additionWithVerification(345, 456)
x = additionWithVerification(567, 879)
print(x,'\n\n')

my_sir_is_a_great_sir = subtractionWithVerification(minuend = 9000, subtrahend = 999)
print(my_sir_is_a_great_sir , '\n\t\t\t\t\t')

yahoo = multiplicationWithVerification(multiplicand = 1283, multiplier = 376)

quotient, reminder = integerDivisionWithVerification(dividend = 9874, divisor = 123)