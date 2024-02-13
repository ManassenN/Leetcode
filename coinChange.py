def coinChange(coins,amount):
        dp = [amount] * (amount + 1)
        dp[0] = 0
        dp[1] = 1

        for target in range(1,amount+1):
            for s in coins:
                coin = target - s
                if coin < 0:
                    break
                dp[target] = min(dp[target],1 + dp[target - s])

        return dp[amount]

coinChange([2],3)