set3 = set( [3*x for x in range( 1, int( 1001/3 )+1 )] )
set7 = set( [7*x for x in range( 1, int( 1001/7 )+1 )] )
set11 = set( [11*x for x in range( 1, int( 1001/11 )+1 )] )

seta = set3 & set7 & set11
setb = (set3 & set7) - set11
setc = set( range( 1, 1001 ) ) - set3 - set7 - set11