def coinChange(coins, amount):
    # Sort coins in descending order to explore larger denominations first
    coins.sort(reverse=True)
    # Initialize a memoization dictionary to store computed results
    memo = {}

    # Define the DFS function with memoization
    def dfs(remaining):
        # If remaining amount is already computed, return it from memo
        if remaining in memo:
            return memo[remaining]
        # Base case: if remaining amount is 0, return 0 coins needed
        if remaining == 0:
            return 0
        # Initialize min_coins with a large value
        min_coins = float('inf')
        # Explore all possibilities with each coin
        for coin in coins:
            # Skip coins larger than the remaining amount
            if coin > remaining:
                continue
            # Explore using this coin and update min_coins
            num_coins = 1 + dfs(remaining - coin)
            min_coins = min(min_coins, num_coins)
        # Store the computed result in memo and return
        memo[remaining] = min_coins
        return min_coins

    # Start DFS with the initial remaining amount
    result = dfs(amount)
    # If result is still float('inf'), it means amount cannot be made up
    if result == float('inf'):
        return -1
    else:
        return result

# Example usage:
coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))  # Output: 3 (11 = 5 + 5 + 1)
