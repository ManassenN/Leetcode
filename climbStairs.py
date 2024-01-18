class Solution(object):
    def climbStairs(self,n):
        # Base cases for 0 and 1 step
        if n == 0 or n == 1:
            return 1

        # Initialize an array to store the number of distinct ways for each step
        dp = [0] * (n + 1)

        # There's only one way to reach the first step
        dp[1] = 1

        # There are two ways to reach the second step: taking 1 step twice or taking 2 steps at once
        dp[2] = 2

        # Calculate the number of distinct ways for each step up to n
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]