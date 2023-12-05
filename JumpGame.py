def canJump(nums):
    n = len(nums)
    if n == 0:
        return False

    # Create an array to store whether it's possible to reach each index
    dp = [False] * n
    dp[0] = True

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if dp[j] and j + nums[j] >= i:
                dp[i] = True
                break

    return dp[n - 1]
canJump([3,2,1,0,4])