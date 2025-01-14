from pcinput import getString

s = getString( "Please enter a string: " )
count = 0
if ("a" in s) or ("A" in s):
    count += 1
if ("e" in s) or ("E" in s):
    count += 1
if ("i" in s) or ("I" in s):
    count += 1
if ("o" in s) or ("O" in s):
    count += 1
if ("u" in s) or ("U" in s):
    count += 1
    
if count == 0:
    print( "There are no vowels in the string." )
elif count == 1:
    print( "There is only one different vowel in the string." )
else:
    print( "There are", count, "different vowels in the string.")