fruitlist = ["apple", "banana", "cherry"]
try:
    num = input( "Please enter a number: " )
    if "." in num:
        num = float( num )
    else:
        num = int( num )
    print( fruitlist[num] )
except:
    print( "Something went wrong" )    