import sys

total = 0
for i in sys.argv[1:]:
    try:
        total += float( sys.argv[i] )
    except TypeError:
        print( sys.argv[i], "is not a number." )
        sys.exit(1)

print( "The arguments add up to", total )