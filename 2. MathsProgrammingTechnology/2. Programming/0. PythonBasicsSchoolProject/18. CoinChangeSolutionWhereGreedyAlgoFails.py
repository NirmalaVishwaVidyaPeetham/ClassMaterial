import math
def minimumCoinsGreedySolution(TotalAmountNeedingChange, ListOfCoinsLargestToSmallest):
    if not (isinstance(TotalAmountNeedingChange,int) and TotalAmountNeedingChange>=0):
        # Same as ' if not isinstance(a,int) or a<0 or a>100: '
        print('Enter an integer >= 0')
        return

    currentAmountRemaining = TotalAmountNeedingChange;
    totalCoinsUsed = 0;
    for coin in ListOfCoinsLargestToSmallest:
        nCoins = currentAmountRemaining//coin;
        totalCoinsUsed = totalCoinsUsed + nCoins;
        print(coin,'cents: ',nCoins, 'coins' )
        currentAmountRemaining = currentAmountRemaining%coin;

    print("Minimum number (greedy solution) of coins for ", TotalAmountNeedingChange, " cents = ", totalCoinsUsed)

## Solution using loops/recursion; Not completed/working yet;
"""
def minimumCoinsLoopsSolution(TotalAmountNeedingChange, listOfCoins):
    if not (isinstance(TotalAmountNeedingChange,int) and TotalAmountNeedingChange>=0):
        # Same as ' if not isinstance(a,int) or a<0 or a>100: '
        print('Enter an integer >= 0')
        return

    currentAmountRemaining = TotalAmountNeedingChange;
    for coin in listOfCoins:
        for nCoins in range(0, 1+TotalAmountNeedingChange//coin):
                    # maximumNumberForEachCoin = TotalAmountNeedingChange//coin
            currentAmountRemaining = TotalAmountNeedingChange - coin*nCoins;

            newListOfCoins = listOfCoins.copy;
            newListOfCoins.remove(coin);
            minimumCoinsLoopsSolution(currentAmountRemaining, newListOfCoins);
"""


## AI solution for minimum: Checked with all our classroom examples and gives the correct values in each case; Algorithm seems to be a dynamic programming style solution.
def min_coins_AI_BottomUp(TotalAmountNeedingChange, ListOfCoins):
    """
    Calculates the minimum number of coins needed to make change.
    Args:
      amount: The amount of change to make.
      ListOfCoins: A list of coin denominations.
    Returns:
      The minimum number of coins needed.
    """
    num_coins = [float('inf')] * (TotalAmountNeedingChange + 1)  # Initialize with infinity
    num_coins[0] = 0  # Base case: 0 coins needed for amount 0
    for coin in ListOfCoins:
        for i in range(coin, TotalAmountNeedingChange + 1):
            num_coins[i] = min(num_coins[i], num_coins[i - coin] + 1)

    min_coins_needed = num_coins[TotalAmountNeedingChange]
    if min_coins_needed != float('inf'):
        print("Minimum coins needed (not greedy):", min_coins_needed)
        return min_coins_needed
    else:
        print("Cannot make change with given denominations.")
        return -1;

minimumCoinsGreedySolution(15, [12, 5, 1])
min_coins_AI_BottomUp(15, [12, 5, 1])


minimumCoinsGreedySolution(71, [11, 10, 1])
min_coins_AI_BottomUp(71, [11, 10, 1])


minimumCoinsGreedySolution(91, [50, 25, 10, 5, 1]);
min_coins_AI_BottomUp(91, [50, 25, 10, 5, 1]);

minimumCoinsGreedySolution(100, [65, 50, 1]);
min_coins_AI_BottomUp(100, [65, 50, 1]);
minimumCoinsGreedySolution(55, [25, 11, 1]);
min_coins_AI_BottomUp(55, [25, 11, 1]);
minimumCoinsGreedySolution(66, [24, 23, 22, 1]);
min_coins_AI_BottomUp(66, [24, 23, 22, 1]);
minimumCoinsGreedySolution(57, [21, 19, 16, 1]);
min_coins_AI_BottomUp(57, [21, 19, 16, 1]);
minimumCoinsGreedySolution(56, [9, 8, 1]);
min_coins_AI_BottomUp(56, [9, 8, 1]);



