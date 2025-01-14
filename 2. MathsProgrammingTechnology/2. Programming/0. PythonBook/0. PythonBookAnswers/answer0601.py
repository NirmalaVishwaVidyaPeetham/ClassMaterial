from pcinput import getFloat

grade = getFloat( "Please enter a grade: " )
check = int( grade * 10 )
if grade < 0 or grade > 10:
    print( "Grades have to be in the range 0 to 10." )
elif check%5 != 0 or check != grade*10:
    print( "Grades should be rounded to the nearest half point.")
elif grade >= 8.5:
    print( "Grade A" )
elif grade >= 7.5:
    print( "Grade B" )
elif grade >= 6.5:
    print( "Grade C" )
elif grade >= 5.5:
    print( "Grade D" )
else:
    print( "Grade F" )