# Write a function that takes "x" as a parameter and prints if "x" is even/odd and if "x" is even it computes "x**2-43*x+42", and if x is odd it computes "x**2-23*x+22"
def even_odd(x):
    if not isinstance(x,int):
        print('Enter an integer')
        return
    if x%2==0:
        print('even')
        y=x**2-43*x+42
        print(y)
    else:
        print('odd')
        y=x**2-23*x+22
        print(y)

even_odd(x=97)
even_odd(x=23)   #odd
even_odd(x=24)  #even
even_odd(x=23)
even_odd(x=289889)
even_odd(x=87)
even_odd(x=-25)  #negative
even_odd(x=-24)
even_odd(x=2778)
even_odd(-649)
even_odd(x=4565465)
even_odd(x=2286)
even_odd(x=-87878777)
even_odd(x=3.4)
print('\n\n\n\n')

# Write a function that takes three integers as paramaters, and prints the largest number of the three integers:
def Largestnumber(a,b,c):
    if not (isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        print('Enter all integers')
        return

    if a>=b and a>=c:
        print(a,' is the largest')
    elif b>=a and b>=c:
        print(b,' is the largest')
    else:
        print(c,' is the largest')

Largestnumber(12, 15, 13)
Largestnumber(5, 12, 3)
Largestnumber(13, 12, 11)
Largestnumber(-1, -234, -486)
Largestnumber(-234, -234, -486)
Largestnumber(12, 12, 11)
Largestnumber(12, 12, 11.35)
print('\n\n\n\n')

# Write a function that takes 3 lenths of a triangle as parameters, and prints "Equilateral", "isosceles, or "scelne" depending on the triangle lenths:
def Give_triangle_lengths(a, b, c):
    # if a<=0 or b<=0 or c<=0:
    # Same as above -- 'not(x and y)' is same as 'not x or not y'
    if not (a > 0 and b > 0 and c > 0):
        print('Enter all three positive lengths')
        return
    #if a==b and b==c and a==c:
    if a == b and b == c:
        print('Equilateral')
    elif a==b or b==c or a==c:
        print('isosceles')
    else:
        print('scalene')
    return
Give_triangle_lengths(a=6, b=2, c=2)
Give_triangle_lengths(a=7.5, b=2.98, c=1.945)
Give_triangle_lengths(a=1, b=1, c=1)
Give_triangle_lengths(a=-1, b=1, c=1)
Give_triangle_lengths(a=-1, b=1, c=0)
print('\n\n\n\n')


# Write a program that takes the x and y coordinates of a point as input and prints the quadrant in which the point lies (first, second, third or fourth) based on x > 0, y > 0; x < 0, y > 0 ; x < 0, y < 0 ; x > 0, y < 0:
def Give_quadrant(x, y):
        # Remember in each case, it's only '>' but not '>='. We learn why when learn coordinate geometry in maths
     if x>0 and y>0:
         print('first quadrant')
     elif x<0 and y>0:
         print('second quadrant')
     elif x<0 and y<0:
         print('third quadrant')
     elif x>0 and y<0:
         print('fourth quadrant')
     else:
         print('No quadrant.')
     return
Give_quadrant(x=-3, y=9)
Give_quadrant(x=2, y=-8)
Give_quadrant(x=2, y=0)
Give_quadrant(x=2, y=-0)
print('\n\n\n\n')

# Write a program that calculates the minimum number of coins needed to make change for a given amount in cents (under 100 cents). Use quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent).
# Below is a 'Greedy' approach that works for these coin denominations, but doesn't work for all denominations. See the notes in for more details.
def minimumCoins(a):
    if not (isinstance(a,int) and a>=0 and a<=100):
        # Same as ' if not isinstance(a,int) or a<0 or a>100: '
        print('Enter an integer between 0 and 100')
        return
    # nQ = number of quarters, remQ is the remainder after quarters
    nQ = a//25
    print(nQ)
    remQ = a%25

    nD = remQ//10
    print(nD)
    remD = remQ%10

    nN = remD//5
    print(nN)
    remN = remD%5

    print(remN)
    # nP = remN // 1 = remN; remP = remN % 1 = 0

    print("Minimum number of coins for ", a, " cents = ", nQ + nD + nN + remN)

minimumCoins(91)
minimumCoins(0)
minimumCoins(100)
minimumCoins(100)
minimumCoins(24)
minimumCoins(38)
minimumCoins(11)
minimumCoins(99)
# Failing cases
minimumCoins(104)
minimumCoins(-234)
minimumCoins(45.6)
minimumCoins(107.6)
minimumCoins(-34.7)
print('\n\n\n\n')







# Write a program that takes a number from 1 to 7 as input, representing the days of the week (1 for Monday, 2 for Tuesday, etc.). Print the corresponding day's name.
def Weekday_caluculater(a):
    #if not (isinstance(a,int) and a>=1 and a<=7):
    # Same as below
    if not isinstance(a, int) or a < 1 or a > 7:
        print('Enter an integer between 1 and 7')
        return

    if a==1:
        print('Monday')
    elif a==2:
        print('Tuesday')
    elif a==3:
        print('Wednesday')
    elif a==4:
        print('Thursday')
    elif a==5:
        print('Friday')
    elif a==6:
        print('Saturday')
    elif a==7:
        print('Sunday')
    else:
        # This is not needed as we are checking it at the beginning
        print('give correct numbers/give a correct number')
    return a

Weekday_caluculater(a=1)
Weekday_caluculater(a=2)
Weekday_caluculater(a=3)
Weekday_caluculater(a=4)
Weekday_caluculater(a=5)
Weekday_caluculater(a=6)
Weekday_caluculater(a=7)
Weekday_caluculater(a=8)
Weekday_caluculater(a=-34.778)
print('\n\n\n\n')


