def knight_dialer(n):
    MOD = 10 ** 9 + 7

    # Define the valid knight moves from each numeric cell
    moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }

    # Initialize a 2D array to store the number of valid phone numbers
    dp = [[0] * 10 for _ in range(n)]

    # Initialize the base case (length 1)
    for i in range(10):
        dp[0][i] = 1

    # Dynamic programming to calculate the number of valid phone numbers
    for length in range(1, n):
        for current_num in range(10):
            for next_num in moves[current_num]:
                dp[length][next_num] = (dp[length][next_num] + dp[length - 1][current_num]) % MOD

    # Sum up the counts for all numeric cells for the given length
    total_count = sum(dp[n - 1]) % MOD

    return total_count

# Example usage:
n = 2
result = knight_dialer(n)
print(result)