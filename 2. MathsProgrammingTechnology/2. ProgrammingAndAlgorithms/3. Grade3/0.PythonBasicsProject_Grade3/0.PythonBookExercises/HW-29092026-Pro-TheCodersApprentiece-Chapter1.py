# Chapter 1:

# Exercise 1.1 
# Get together with another person, and do the following exercise. Get four playing cards with different values. Shuffle them, and put them face-down on the table. One of you has to sort the cards, from low to high. This person is allowed to move the cards around, but is not allowed to look at their face sides. However, this person is allowed to point at two of the cards, after which the other one picks up those two cards, looks at their faces, and then puts them back and says which of the two is higher. Count how often such a comparison is made. Once the first person is satisfied that the cards are sorted, they are turned over to check if they are indeed sorted correctly. In this exercise, the first  person basically takes the role of a computer program, that follows instructions without actually understanding values. The second person takes the role of the computer processor, which can perform certain functions for the program, in  this case, comparing numbers. If you did not manage to sort the cards correctly, think about how you can accomplish this task under the given circumstances, and after that try it once more. If you did sort them correctly and needed more than six comparisons, think about how you can do it with six comparisons. If you managed to do it with six comparisons, think about if you can do it with less than six. If you did it with less than six, think about if your procedure is guaranteed to sort any collection of four cards.

# Note: Exercise 1.1 is to do the instructions from Exercise 1.2.



# Exercise 1.2 Write down exact instructions, in plain English, on how to sort cards under the circumstances described above. Get a third person and ask this person to take your instructions and follow them, while one of you two takes the role of processor. Ask the third person to perform the steps as literally as possible, without trying to interpret meaning. This exercise is most illustrative if the third person has no idea what the exact function of the instructions is. Once the sorting procedure has finished, check if the result is correct.

# P1: Role of a program
# P2: Role of the processer

# We have 4 cards.

# Instructions:
# Step 1: P1 takes any 2 cards and asks P2 which one is bigger.
# Step 2: P1 puts the smaller card on the left and the larger card to the right in bunch B1 and the other 2 cards in the other bunch B2.
# Step 3: P1 takes the 2 cards, the leftmost one in B1 and a random card from B2 and asks P2 to compare.
# Step 4: If the card from the bunch B2 is smaller or equal, P1 puts it to leftmost in B1.
# Step 5: If the card from the bunch B2 is bigger, P1 asks P2 to compare it with the rightmost card in B1.
# Step 6: If the card from B2 is bigger, P1 puts it as the rightmost card in B1; otherwise, P1 puts it in between the 2 cards in B1.
# Step 7: Now, P1 asks P2 to compare the remaining card in B2 with the leftmost card in B1.
# Step 8: If the card from B2 is smaller than the leftmost card in B1, P1 places it as the leftmost card in B1.
# Step 9: Otherwise, P1 asks P2 to compare it with the middle card in B1.
# Step 10: If the card from B2 is smaller than the middle card in B1, P1 places it as the card in between leftmost card and middle card in B1.
# Step 11: Otherwise, P1 asks P2 to compare it with the rightmost card in B1.
# Step 12: If the card from B2 is smaller than the rightmost card, then P1 places it in between the middle and the right card in B1.
# Step 13: If the card from B2 is bigger than the rightmost card, then P1 places it as the rightmost card in B1.
# Your cards are sorted in ascending order!