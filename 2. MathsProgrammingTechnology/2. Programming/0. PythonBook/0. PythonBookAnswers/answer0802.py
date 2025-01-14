from pcinput import getString

# commoncharacters gets two strings as parameters.
# It returns the number of characters that they have in common.
def commoncharacters( w1, w2 ):
    common = ""
    for letter in w1:
        if (letter in w2) and (letter not in common):
            common += letter
    return len( common )

word1 = getString( "Give word 1: " )
word2 = getString( "Give word 2: " )

num = commoncharacters( word1, word2 )
if num <= 0:
    print( "The words share no characters." )
elif num == 1:
    print( "The words have one character in common" )
else:
    print( "The words have", num, "characters in common")