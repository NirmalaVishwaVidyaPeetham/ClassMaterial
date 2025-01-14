from pcinput import getInteger

TOTAL = 10
largest = 0
smallest = 0
div3 = 0

for i in range( TOTAL ):
    num = getInteger( "Please enter number "+str( i+1 )+": " )
    if num%3 == 0:
        div3 += 1
    if i == 0:
        smallest = num
        largest = num
        continue
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
        
print( "Smallest is", smallest )
print( "Largest is", largest )
print( "Dividable by 3 is", div3 )