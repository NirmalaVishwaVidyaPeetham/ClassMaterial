import sys

# 3 variables for holding the command line parameters
inputfile = "input.txt"
outputfile = "output.txt"
shift = 3

# Processing the command line parameters 
# (works with 0, 1, 2, or 3 parameters)
if len( sys.argv ) > 1:
    inputfile = sys.argv[1]
if len( sys.argv ) > 2:
    outputfile = sys.argv[2]
if len( sys.argv ) > 3:
    try:
        shift = int( sys.argv[3] )
    except TypeError:
        print( sys.argv[3], "is not an integer." )
        sys.exit(1)