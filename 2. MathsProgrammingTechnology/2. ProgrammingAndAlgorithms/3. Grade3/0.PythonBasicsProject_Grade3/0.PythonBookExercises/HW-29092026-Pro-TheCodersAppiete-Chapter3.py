# Chapter 3:

#  if you type the following command in the shell and
# press Enter, you see the result 12.
5 + 7

# The print function is used as follows: you write the word print, followed by an opening parenthesis, followed by whatever you want to display, followed by a closing parenthesis. For example (and I showed this one before):

print("Hello, world")
# -----------------------

# You can display multiple things with one print() function by putting everything that you want to display between the parentheses with commas in between. The print() function will then display all of the items, with one space in between each pair or them. For example

print( "I", "own",  "two", "apples", "and", "one", "banana" )

# -------------------------------------

# Note that the spaces in this statement are all superfluous.

print("I","own","two","apples","and","one","banana")

# -------------------------------------

# Note that you can not only use print() to display texts, but also to display numbers. You can even mix them up, as the following code shows.

print( "I", "own", 2, "apples", "and", 1, "banana" )

#----------

# Exercise Display some texts of your liking using a Python program. But take note that if you want to display text strings, you have to enclose them in double quotes – or single
# quotes, those work too.

print("I", "am", "happy.")

# ------------------

# What if a string contains both double quotes and single quotes? You can solve that issue by putting a backslash (\) in front of the single or double quote that is part of the string to tell Python to treat that single or double quote as a character of the string rather than something that ends the string, i.e., 'I can\'t stand it' is a legal string. You can see that when you try to print it:

print( ' I can\'t stand it ' )

# --------------

# But what if I want to put an actual backslash in a string, and that backslash is, by chance, in front of a single or double quote? Well, I can do the same thing for a backslash, namely put a backslash in front of a backslash to make it a literal backslash, rather than a backslash that changes the interpretation of the character that comes after it. For an example, check out what the next bit of code displays (you can type it into the Python shell).

print( ' I can\\\'t stand it ' )

# -----------------------------------

# Check out the following code and think about what it will display when you run it. Then copy it to the Python shell and run it.

print(1,000,000,000) # no commas allowed

# --------------------------------------

# Basic calculations combine two values with one operator in between them.
# Some straightforward operators are:
# + addition
# - subtraction
# * multiplication
# / division
# // integer division
# ** power
# % modulo
# Here are some examples:
print( 15+4 )
print( 15-4 )
print( 15*4 )
print( 15/4 )
print( 15//4 )
print( 15**4 )
print( 15%4 )

# -----------------------------

# Check out the calculation below, and try to predict what it will result in before you copy it to the Python shell and run the code.

print( 5*2 -3+4/2 ) # 9.0 (there's no integer division)

# -----------------

# Second, just as explained above, spaces are ignored by Python, so the code above is the same as:
print( 5 * 2 - 3 + 4 / 2 )

# ---------------------------

# It is even the same as:

print( 5*2 - 3+4 / 2 )

# -----------------

# I have been in long discussions with people who keep arguing that the code above should result in 6.5 or 1.5, because clearly you have to calculate the 5 ∗ 2 and the 3 + 4 before you do the subtraction and division. That is hogwash. It does not matter how close you place operands together, spaces are ignored. If you really want to calculate the 3 + 4 first, you have to put it between parentheses. You can then still use spaces to improve readability, but they mean nothing to Python.

print( (5*2) - (3+4) /2 )
print( ((5*2) -(3+4)) / 2 )

# ---------------

# Exercise Now it is time to write your first program. Write a program that displays the number of seconds in a week. You should, of course, not grab your calculator or smartphone to do the calculation and then just print the resulting number, but you should do the calculation in Python code. Since this program needs only one line of code, you could just write it in the Python shell, though you are encouraged to create a program file and use that.

print(f"There are {7*24*60*60} seconds in one week.")

#---------------

# In particular, you can use the addition operator (+) to concatenate two strings, and you can use the multiplication operator (∗) with a number and a string to create a string that contains a repetition of the original string. Check it out:
print( "hello"+"world" )
print( 3* "hello" )
print( "goodbye" *3 )

# --------------------------

# See the difference between the following two lines of code:

print( 15/4 )
print( int( 15/4 ) )

# --------------------

# Or the following two lines of code:

print( 15+4 )
print( float( 15+4 ) )

# -----------------

# I stated that you cannot use the addition operator to concatenate a number to a string. However, if you need to do something like that, you can work around the issue by using string type casting:

print( "I own " + str( 15 ) + " apples." )

# -------------------

# Most of these things are just “style.” The white spaces next to the parentheses and around operators are not necessary, Python understands the code just as well when they are gone. These four statements are all equivalent:

print( 2 + 3 )
print(2+3)
print( 2+3)
print ( 2 + 3 )

# ----------------

# Exercise 3.1 The cover price of a book is $24.95, but bookstores get a 40 percent discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. Calculate the total wholesale costs for 60 copies.

bookCostForTheStore = 24.95 - (40/100)*24.95
totalNumberOfBooks = 60
costForAllTheBooks = totalNumberOfBooks * bookCostForTheStore
totalShippingCost = 3 + 0.75*(totalNumberOfBooks-1)
totalCost = costForAllTheBooks + totalShippingCost
print(f"Total cost: ${totalCost}")

# ---------------

#Exercise 3.2 Can you identify and explain the errors in the following lines of code? Correct them.

# print( "A message" ). -> dot at the end; should be 'print( "A message" )'
# print( "A message ' ) -> not ending with double quotes; should be 'print( "A message " )'
# print( ' A messagef" ' ) -> extra double quote; should be 'print( ' A messagef ' )'

# ------------------

# Exercise 3.3 When something is wrong with your code, Python will raise errors. Often these will be “syntax errors” that signal that something is wrong with the form of your code (e.g., the code in the previous exercise raised a SyntaxError). There are also “runtime errors,” which signal that your code was in itself formally correct, but that something went wrong during the code’s execution. A good example is the ZeroDivisionError, which indicates that you tried to divide a number by zero (which, as you may know, is not allowed). Try to make Python raise such a ZeroDivisionError.

# print(5/0)

# -----------------

# Exercise 3.4 Here is another illustrative example of a runtime error. Run the follow code and study the error that it generates. Can you locate the problem?

# print( ((2*3) /4 + (5 -6/7) *8 ) -> ')' not there.
print( ((12*13) /14 + (15 -16) /17) *18 ) # no problem?

# -----------

# Exercise 3.5 You look at the clock and see that it is currently 14.00h. You set an alarm to go off 535 hours later. At what time will the alarm go off? Write a program that prints the answer. Hint: for the best solution, you will need the modulo operator.

sum = 535 + 14  # Computing the time from 00 hours of today, not from the current time
    # Eg: if alarm set for 11 hours from now (now is 14:00), then we want tomorrow at 01:00 as the answer, not 0 days and 11 hours from now
number_of_days = sum // 24
number_of_hours = sum % 24
print(f"The alarm will go off {number_of_days} days from today and at {number_of_hours} hours.")