try:
    fp = open( "pc_rose.txt" )
    print( "File opened" )
    print( fp.read() )
finally:
    fp.close()
    print( "File closed" )