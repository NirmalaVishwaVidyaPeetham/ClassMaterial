try:
    print( 3 / int( input( "Please enter a number: " ) ) )
except ZeroDivisionError:
    print( "Dividing by zero is not allowed" )
except ValueError:
    print( "You have not entered an integer" )
print( "Goodbye!" )