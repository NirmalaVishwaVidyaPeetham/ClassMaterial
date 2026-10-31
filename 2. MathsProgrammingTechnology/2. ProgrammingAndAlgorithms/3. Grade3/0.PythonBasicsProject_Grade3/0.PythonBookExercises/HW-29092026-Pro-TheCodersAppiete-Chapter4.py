# Chapter 4:
from numpy.ma.extras import average

# To create a variable (i.e., choose the variable name), you must “assign” it a value. The assign-operator is the equals (=) symbol. To the left of it you put the variable name, and to the right of it you put the value that you want to store in the variable. This is best illustrated with an example:

x = 5
print( x )

# -----------

# Exercise In the previous chapter you wrote a calculation that determines the number of seconds in a week. Copy this calculation into a program, and assign it to a variable. Then add a statement to print the contents of the variable.

x = 7 * 24 * 60 * 60

print(f"There are {x} seconds in one week.")

# -------------

# When you assign a value to a variable name in your program, the first time you do that for a specific varible name, it creates the variable. If later in the program you assign another value to the same variable name, it “overwrites” the previous value. In the box metaphor: you empty the box and put something else in it. A variable always holds the value that was last assigned to it.

x = 5
print( x )
x = 7 * 9 + 13 # overwrite the previous value of x
print( x )
x = "A nod ' s as good as a wink to a blind bat."
print( x )
x = int( 15 / 4 ) - 27
print( x )

# ----------------

# Once a variable is created (and thus has a value), you can use it in your code where you otherwise would use values. You can, for instance, use it in calculations.

x = 2
y = 3
print( "x =", x )
print( "y =", y )
print( "x * y =", x * y )
print( "x + y =", x + y )

# -------

# You may copy the contents from one variable to another, using the assignment operator

x = 2
y = 3
print( "x =", x, "and y =", y )
# Swap the values of x and y using z as intermediary storage.
z = x
x = y
y = z
print( "x =", x, "and y =", y )

# -----------

# When you assign something to a variable, you might even use the variable itself on the right-hand side of the assignment operator, provided it was created earlier. The right-hand side of an assignment is always evaluated completely before the actual assignment takes place.

x = 2
print( x )
x = x + 3
print( x )

# Note that a variable must be created before you can use it! Running the following code will result in an error, because days_in_a_year has not (yet) been created before I use it on the first line:

# print( days_in_a_year )
# days_in_a_year = 365

# ----------------

# You should try to stick to these conventions for your own code. In particular the convention of choosing meaningful variable names is important to follow, because meaningful variable names make code readable and maintainable. Look, for instance, at the following code:

a = 3.14159265
b = 7.5
c = 8.25
d = a * b * b * c / 3
print( d )

# ------

# Now look at the following, equivalent code:

pi = 3.14159265
radius = 7.5
height = 8.25
volume_of_cone = pi * radius * radius * height / 3
print( volume_of_cone )

# ---------

# Exercise In the code block below, the value 1 is assigned to a number of (potential) variable names. Some of these are legal, others are not. Identify the illegal variable names, and explain why they are illegal.
classification = 1 # 1
Classification = 1 # 2
# cl@ssification = 1 # 3 -> no @s allowed.
class1f1cat10n = 1 # 4
# 1classification = 1 # 5 -> variable should start with a letter or _.
_classification = 1 # 6
# class = 1 # 7 -> class is a keyword
Class = 1 # 8

# -----------

# Constants can be useful to make code more readable. For instance, to calculate the total of a bill of 24.95 EUR with a 15% service charge, you can use:

total = 24.95
final_total = int( 100 * total * 1.15 ) / 100
print( final_total )

# --------

# However, it is more readable to write:

SERVICE_CHARGE = 1.15
CENTS = 100
total = 24.95
final_total = int( CENTS * total * SERVICE_CHARGE ) / CENTS
print( final_total )

# --------------

# Typically, when things go wrong in a program, the reason is that variables are holding values that you did not expect them to have when writing the code. A good way of “debugging” your code (i.e., finding out where problems are and fixing them) is printing the variable names and values in appropriate places. For instance, the following code gives an error when you run it.

nr1 = 5
nr2 = 4
nr3 = 5
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
nr1 = nr1 + 1
print(nr1, nr2, nr3)
print( nr3 / (nr1 % nr2) )

# --------

# The types that you have seen until now are integer, float, and string. You can use the function type() to see what the type of a variable is.

a = 3
print( type( a ) )
a = 3.0
print( type( a ) )
a = "3.0"
print( type( a ) )

# ----------

# Since variables have a type, the effect of operators might change depending on the types of the variables involved. For instance, in the following code, the addition operator (+) is used twice, but its effect changes due to the types of the variables involved.

a = 1
b = 4
c = "1"
d = "4"
print( a + b )
print( c + d )

# ---------

# Exercise In the code above, what would happen if you try to print a + c? If you do not know, try it.

# print(a + c) -> it gives error: "TypeError: unsupported operand type(s) for +: 'int' and 'str'"

# --------

# Exercise What does the code given below display? First think about it, then run the code, and make sure that you understand what happens.

name = "John Cleese"
print( "name" ) # -> prints name, not John Cleese; because name is in double quotes.
# ------------

# Exercise Change the code above so that it displays the name of a famous member of Monty Python.

# TODO: Who is the famous member of Monty Python?

# --------

# Since version 3.5 of Python, it is possible to add “type hints” to your code. When you first use a variable name, you follow it by a colon and the name of the type, to indicate what type the variable is supposed to be. For instance, the following code makes explicit that you want a to be an integer, and b to be a string.

a: int = 1
b: str = "4"
print( type(a), type(b))

# ---------

# However, such type hints are no more than annotations. Python ignores such annotations. For instance, even if the annotations say that a should be an integer, and b should be a string, you can assign a string to a and an integer to b.

a: int = "1"
b: str = 4
print( type(a), type(b) )

# -----

# The following code:

number_of_bananas = 100
number_of_bananas = number_of_bananas + 1
print( number_of_bananas )

# is equivalent to:

number_of_bananas = 100
number_of_bananas += 1
print( number_of_bananas )

# -------

# Exercise What will the code given below display? Run it to see if you are correct.

number_of_bananas = 100
number_of_bananas += 12
number_of_bananas -= 13
number_of_bananas *= 19
number_of_bananas /= number_of_bananas
print( number_of_bananas ) # -> prints 1.0 because decimal division

# ------

# Learn more about comments by studying the code below.

# comment: insert your code here.
# BTW: Have you noticed that everything right of the hash mark
print( "Something..." ) # is ignored by your python interpreter?
print( "and something else.." ) # Use this to comment your code!
"""Another way of commenting on your code is via triple quotes
-- these can be distributed over multiple """ # lines
' ' ' which can also be done with single quotes ' ' ' # but be careful
# with there being quotes IN your comments when you use this
# multi -line method
print( "Done." )

# ----- Exercises -----

# Define three variables var1, var2 and var3. Calculate the average of these variables and assign it to average. Print the average. Add three comments.
# (Note: Average = All items added ÷ Number of items)
var1 = 5
var2 = 4
var3 = 3
average = ( var1 + var2 + var3 ) / 3
print(f"The average of {var1}, {var2}, and {var3} is: {average}")
# Step 1: Calculates the average of var1, var2, and var3.
# Step 2: Assigns the average to the variable "average"
# Step 3: Prints the average of var1, var2, and var3.

# ----------

#Write code that can compute the surface of circle, using the variables radius and pi = 3.14159. The formula, in case you do not know, is radius times radius times pi. Print the outcome of your program as follows: “The surface area of a circle with radius ... is ...”

radius = 4
pi = 3.14159
print(f"The surface area of a circle with radius {radius} is: {pi * radius**2}")

# -----------

# Write code that classifies a given amount of money (which you store in a variable named amount), specified in cents, as greater monetary units. Your code lists the monetary equivalent in dollars (100 ct), quarters (25 ct), dimes (10 ct), nickels (5 ct), and pennies (1 ct). Your program should report the maximum number of dollars that fit in the amount, then the maximum number of quarters that fit in the remainder after you subtract the dollars, then the maximum number of dimes that fit in the remainder after you subtract the dollars and quarters, and so on for nickels and pennies. The result is that you express the amount as the minimum number of coins needed.

amount = 1089
no_of_dollars = amount // 100
no_of_quarters = (amount - no_of_dollars * 100) // 25
no_of_dimes = (amount - no_of_dollars * 100 - no_of_quarters * 25) // 10
no_of_nickels = (amount - no_of_dollars * 100 - no_of_quarters * 25 - no_of_dimes * 10) // 5
no_of_pennies = (amount - no_of_dollars * 100 - no_of_quarters * 25 - no_of_dimes * 10 - no_of_nickels * 5) // 1
print(f"{amount} = ${no_of_dollars} + {no_of_quarters} quarters + {no_of_dimes} dimes + {no_of_nickels} nickels + {no_of_pennies} pennies")
# -------
# Can you think of a way to swap the values of two variables that does not need a third variable as a temporary storage? In the code block below, try to implement the swapping of the values of a and b without using a third variable. To help you out, the first step to do this is already given. You just need to add two more lines of code.

a = 17
b = 23
print( "a =", a, "and b =", b )
a += b
# add two more lines of code here to cause swapping of a and b
# TODO: I need help.
print( "a =", a, "and b =", b )