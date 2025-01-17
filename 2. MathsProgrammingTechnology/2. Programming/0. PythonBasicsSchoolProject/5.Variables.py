# Datatypes: int, float, string

myDollars = 200
dollarToRupees = 80
dollarToEuros = 1.2
dollarToYen = 8.7

print('My dollars give me '+ str(myDollars*dollarToRupees) + ' rupees')
print('My dollars give me '+ str(myDollars*dollarToEuros) + ' euros')
print('My dollars give me '+ str(myDollars*dollarToYen) + ' yens')

whichTable = 1000000

for i in range(10):
    print(whichTable*(i+1))
