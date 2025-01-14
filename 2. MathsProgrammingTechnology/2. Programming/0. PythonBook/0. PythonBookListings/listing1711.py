def getStringLenMax10( prompt ):
    s = input( prompt )
    if len( s ) > 10:
        raise ValueError( "Length exceeds 10", len( s ) )
    return s

print( getStringLenMax10( "Use 10 characters or less: " ) )