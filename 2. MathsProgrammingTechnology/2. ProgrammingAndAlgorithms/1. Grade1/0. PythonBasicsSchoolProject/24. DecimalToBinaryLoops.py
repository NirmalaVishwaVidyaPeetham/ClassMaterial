def convertToAnyBase(decimalNumber, base):
    binaryList = []
    currentNumber = decimalNumber
    while currentNumber > 0:
        currentLastDigit = currentNumber%base;
        binaryList = [currentLastDigit] + binaryList;
        currentNumber = currentNumber//base;
    return binaryList

def convertBaseListToDecimal(listInBase, base):
    decimalValue = 0;
    for i in range(0, len(listInBase)):
        decimalValue += listInBase[i]*(base**(len(listInBase)-1-i));
    return decimalValue;

originalDecimalNumber = 23;

base10List = convertToAnyBase(originalDecimalNumber,10);
base10ListDecimalValue = convertBaseListToDecimal(base10List, 10)
print(base10List, base10ListDecimalValue)

base2List = convertToAnyBase(originalDecimalNumber,2);
base2ListDecimalValue = convertBaseListToDecimal(base2List, 2)
print(base2List, base2ListDecimalValue)

base9List = convertToAnyBase(originalDecimalNumber,9);
base9ListDecimalValue = convertBaseListToDecimal(base9List, 9)
print(base9List, base9ListDecimalValue)
