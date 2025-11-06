for i in "apple":
    print(i)
# Iterates over the characters in the string and prints them one per line.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Here it iterates over the list of strings, and prints one string per line.

len(fruits)
    # prints the number of elements/items in the list


for i in range(10,1,-1):
    print(i)
# Prints 10, 9,..., 2

i= 10
while i > 1:
    print(i)
    i = i - 1
# Prints 10, 9,..., 2
# Explanation of the conversion:
# # Initialization: The for loop starts with i being initialized to 10. We replicate this by setting i = 10 before the while loop begins.
# Condition: The for loop continues as long as i is within the range 10 down to (but not including) 1. In the while loop, we express this condition as i > 1. The loop will keep running as long as i is greater than 1.
# Update: The for loop decrements i by 1 in each iteration (-1 step in range). We achieve the same in the while loop by including the statement i -= 1 at the end of the loop's body.

for i in range(1,11):
    print(i)
    i+=1
    # That code will print the numbers from 1 to 10, each on a new line.
    # Here's why:
    # for i in range(1, 11):: This loop starts by initializing the variable i to 1. The range(1, 11) function generates a sequence of numbers starting from 1 and going up to (but not including) 11. So, in the first iteration, i is 1.
    # print(i): This line prints the current value of i.
    # i += 1: This line increments the value of i by 1. However, in a for loop, the loop variable (i in this case) is automatically managed by the range() function for the next iteration. So, while you are changing the value of i within the loop's body, it will be reassigned to the next value in the range(1, 11) sequence at the beginning of the subsequent iteration.
    # Therefore, the i += 1 inside the loop doesn't affect the sequence of numbers that the for loop iterates through. The range(1, 11) dictates that i will take on the values 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10 in successive iterations.