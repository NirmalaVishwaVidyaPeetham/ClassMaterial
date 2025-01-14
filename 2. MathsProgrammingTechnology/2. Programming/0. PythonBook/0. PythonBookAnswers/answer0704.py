bottles = 10
s = "s"

while bottles != "no":
    print( "{0} bottle{1} of beer on the wall, "\
        "{0} bottle{1} of beer.".format( bottles, s ) )
    bottles -= 1
    if bottles == 1:
        s = ""
    elif bottles == 0:
        s = "s"
        bottles = "no"
    print( "Take one down, pass it around, {} bottle{} "\
        "of beer on the wall.".format( bottles, s ) )