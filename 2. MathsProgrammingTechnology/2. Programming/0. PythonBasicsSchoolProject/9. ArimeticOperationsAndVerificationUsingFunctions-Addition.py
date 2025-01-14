
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


additionWithVerification(9846, 807)
x = additionWithVerification(345, 456)
x = additionWithVerification(567, 879)

print(x,'\n\n')
