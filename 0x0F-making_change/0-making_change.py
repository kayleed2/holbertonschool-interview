#!/usr/bin/python3
# Given a pile of coins of 
# different values, determine 
# the fewest number of coins needed to 
# meet a given amount total.

def makeChange(coins, total):
    # If total is 0 or less, return 0
    if total <= 0:
        return 0
    
    # Initialize the array to store the minimum number of coins needed to make each amount
    dp = [float('inf')] * (total + 1)
    # The minimum number of coins needed to make 0 is 0
    dp[0] = 0
    
    # Loop through all the coin values
    for coin in coins:
        # Loop through all the amounts starting from the coin value
        for i in range(coin, total + 1):
            # Calculate the minimum number of coins needed to make the amount
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If total cannot be met by any number of coins you have, return -1
    if dp[total] == float('inf'):
        return -1
    
    # Return the fewest number of coins needed to meet total
    return dp[total]
