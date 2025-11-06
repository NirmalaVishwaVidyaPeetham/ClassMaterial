# 6. Average of Positive Numbers:
# Write a program that repeatedly takes input from the user until they enter a negative number. Use a while loop and calculate the average of all positive numbers entered.
# Hint: Average means sum(items)/numberOfItems. It's also called 'mean'. Eg: If there are 4 students in a class, each scoring 35, 40, 25, 30 points, then the average points for the class = (35+40+25+30)/4 = 130/4 = 32.5

print("Enter a list of non-negative integers one by one, to find their average. Enter a negative number when your list is complete.")
currentNumber = 1;
sum = 0; listSize = 0;
while currentNumber>=0:
    currentNumber = int(input("Enter a number>=0: "))
    if currentNumber >= 0:
        sum += currentNumber
        listSize+=1
    else:
        print("Average of the list of numbers = " , sum/listSize)


# 7. Fibonacci Sequence:
# Write a program that uses a for loop to generate the first 'n' numbers of the Fibonacci sequence (e.g., 0, 1, 1, 2, 3, 5, 8...).
# Hint: First two elements of the list are [0,1]. From the third element onwards, list(i) = list(i-1)+list(i-2);

# 10. Pattern Printing (Nested Loops and Continue):
# Write a nested loop that prints the following pattern:
# ```
# 1
# 1 3
# 1 3 5
# 1 3 5 7
# ```
# * Use a `continue` statement to skip even numbers.
# Hint: Use two loops - one for rows, another for columns