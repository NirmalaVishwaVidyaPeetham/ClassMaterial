import re

# List of strings used for testing.
slist = [ "aaabbb", "aaaaaa", "abbaba", "aaa", "gErbil ottEr",
    "tango samba rumba", " hello world ", " Hello World " ]

# List of regular expressions to be completed by the student.
relist = [
    r"^a*b*$",            # 1. Only a's followed by only b's, including ""
    r"^a*$",              # 2. Only a's, including ""
    r"^[ab]*$",           # 3. Only a's and b's, in any order, including "" 
    r"^aaa$",             # 4. Exactly three a's
    r"^[^ab]*$",          # 5. Neither a's nor b's, but "" allowed
    r"^(aa)*$",           # 6. An even number of a's (and nothing else)
    r"^\s*\S+\s+\S+\s*$", # 7. Exactly two words, regardless of white spaces
    r"ba\b",              # 8. Contains a word that ends in "ba"
    r"\b[A-Z]"            # 9. Contains a word that starts with a capital
]

for s in slist:
    print( s, ':', sep='', end=' ' )
    for i in range( len( relist ) ):
        m = re.search( relist[i], s )
        if m:
            print( i+1, end=' ' )
    print()