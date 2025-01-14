numlist = [ 100, 101, 0, "103", 104 ]
try:
    i1 = int( input( "Give an index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )
except ValueError:
    print( "You did not enter an integer" )
except IndexError:
    print( "You should specify an index between -5 and 4" )
except ZeroDivisionError:
    print( "It looks like the list contains a zero" )
except TypeError:
    print( "it looks like there is a non-numeric item" )
except:
    print( "Something unexpected happened" )
    raise