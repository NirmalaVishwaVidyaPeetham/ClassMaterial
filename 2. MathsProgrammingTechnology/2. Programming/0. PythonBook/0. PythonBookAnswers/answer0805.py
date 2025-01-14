from pcinput import getInteger

def getNumber( prompt ):
    while True:
        num = getInteger( prompt )
        if num < 0 or num > 1000:
            print( "Please enter a number between 0 and 1000" )
            continue
        return num

def main():
    while True:
        x = getNumber( "Enter number 1: " )
        if x == 0:
            break
        y = getNumber( "Enter number 2: " )
        if y == 0:
            break
        if x%y == 0 or y%x == 0:
            print( "Error: the numbers cannot be dividers" )
            return
        print( "Multiplication of", x, "and", y, "gives", x * y )
    print( "Goodbye!" )

if __name__ == '__main__':
    main()