def mixed_key( element ):
    if isinstance( element, str ):
        return 1, element
    return 0, element

mixedlist = ["apple", 0, "strawberry", 5, "banana", 2, \
"raspberry", 9, "cherry", "banana", 7, 7, 6, "blueberry"]
mixedlist.sort( key=mixed_key )
print( mixedlist )