def multiply_xyz( x, y=1, z=7 ):
    print( x * y * z )
    
multiply_xyz( 2, 2, 2 ) # x=2, y=2, z=2
multiply_xyz( 2, 5 )    # x=2, y=5, z=7
multiply_xyz( 2, z=5 )  # x=2, y=1, z=5