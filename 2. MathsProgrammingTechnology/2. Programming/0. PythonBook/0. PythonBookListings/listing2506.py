import re

# List of strings used for testing.
slist = [ "aaabbb", "aaaaaa", "abbaba", "aaa", "gErbil ottEr",
    "tango samba rumba", " hello world ", " Hello World " ]

# List of regular expressions to be completed by the student.
relist = [
    r"",  # 1. Only a's followed by only b's, including ""
    r"",  # 2. Only a's, including ""
    r"",  # 3. Only a's and b's, in any order, including "" 
    r"",  # 4. Exactly three a's
    r"",  # 5. Neither a's nor b's, but "" allowed
    r"",  # 6. An even number of a's (and nothing else)
    r"",  # 7. Exactly two words, regardless of white spaces
    r"",  # 8. Contains a word that ends in "ba"
    r""   # 9. Contains a word that starts with a capital
]

for s in slist:
    print( s, ':', sep='', end=' ' )
    for i in range( len( relist ) ):
        m = re.search( relist[i], s )
        if m:
            print( i+1, end=' ' )
    print()