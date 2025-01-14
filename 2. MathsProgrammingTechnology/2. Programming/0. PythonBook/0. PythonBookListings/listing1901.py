def getRGB( color ):
    blue = color & 255
    green = (color >> 8) & 255
    red = (color >> 16) & 255
    return red, green, blue
    
r, g, b = getRGB( 223567 )
print( "red={}, green={}, blue={}".format( r, g, b ) )