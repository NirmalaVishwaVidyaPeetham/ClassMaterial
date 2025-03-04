
import time;

# range(start,end,step) is a function which gives you numbers from start, in increasing order by a value of step, until <end value
print(list(range(23, 56, 2)))
    # [23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55]
print(list(range(23, 56, 45)))
    # [23]

range(3)
    # = range(0, 3) = [0, 1, 2]

for i in range(1,10):
    print(i);

for i in [1,2,3,45,34]:
    print(i);

for i in ["dfa", 23, 34.5, True]:
    print(i);

while True:
    print('new iteration');
    time.sleep(1) # waits for 1 second without doing anything

# Print 1 to 10 using while loop
valueToPrint=1
shouldIPrintOrStop=True;
while shouldIPrintOrStop:
    print("Before increment:",valueToPrint, shouldIPrintOrStop)
    valueToPrint = valueToPrint + 1;
    if valueToPrint==11:
        shouldIPrintOrStop = False;
    print("After increment:", valueToPrint, shouldIPrintOrStop)
    time.sleep(1)   # Adding this so we can see the output, else it is too fast to see

# Prints 1 to 4, skips 5 to 10
for i in range(1,11):
    if i == 5:
        break;
    print(i);

# Prints 1 to 10, skips only 5
for i in range(1,11):
    if i == 5:
        continue;
    print(i);


for i in range(1,11):
    for j in range(1,11):
        print(i," ", j);

# Multiplication table for 5
for i in range(1,21,1):
    print("5 x ",i," = ", 5*i);

# Multiplication table for 5 using only additions and no multiplications
multiplicationValue = 0;
for i in range(1,21,1):
    multiplicationValue = multiplicationValue + 5;
    print("5 x ",i," = ", multiplicationValue);

