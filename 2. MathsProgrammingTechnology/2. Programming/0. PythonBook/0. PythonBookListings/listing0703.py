from pcinput import getInteger
    
num = -1
total = 0
while num != 0:
    num = getInteger( "Enter a number: " )
    total += num
print( "Total is", total )