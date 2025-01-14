CENTS_IN_DOLLAR = 100
CENTS_IN_QUARTER = 25
CENTS_IN_DIME = 10
CENTS_IN_NICKEL = 5

amount = 1156
cents = amount

dollars = int( cents / CENTS_IN_DOLLAR )
cents -= dollars * CENTS_IN_DOLLAR
quarters = int( cents / CENTS_IN_QUARTER )
cents -= quarters * CENTS_IN_QUARTER
dimes = int( cents / CENTS_IN_DIME )
cents -= dimes * CENTS_IN_DIME
nickels = int( cents / CENTS_IN_NICKEL )
cents -= nickels * CENTS_IN_NICKEL
cents = int( cents )

print( amount / CENTS_IN_DOLLAR, "consists of:" )
print( "Dollars:", dollars )
print( "Quarters:", quarters )
print( "Dimes:", dimes )
print( "Nickels:", nickels )
print( "Pennies:", cents )
