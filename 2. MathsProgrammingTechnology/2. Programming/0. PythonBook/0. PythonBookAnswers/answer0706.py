from pcinput import getString

word1 = getString( "Give word 1: " )
word2 = getString( "Give word 2: " )
common = ""
for letter in word1:
    if (letter in word2) and (letter not in common):
        common += letter
if common == "":
    print( "The words share no characters." )
else:
    print( "The words have the following in common:", common )