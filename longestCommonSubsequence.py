def longestCommonSubsequence(text1: str, text2: str) -> int:
        # Initialize matrix with rows and columns based on string lengths
        m,n = len(text1), len(text2)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        if text1[0] == text2[0]:
            dp[0][0] = 1

        # Fill the first row
        for i in range(1,max(len(text2),len(text1))):
            if text2[0] == text1[i]:
                dp[0][i]=dp[0][i-1] + 1 
            else:
                dp[0][i] = dp[0][i-1]    

        # Fill the first column
        for i in range(1,min(len(text2),len(text1))):
            if text1[0] == text2[i]:
                dp[i][0] = dp[i-1][0] + 1
            else:
                dp[i][0] = dp[i-1][0]

        # Fill the rest of the matrix
        for i in range(1,len(text1)):
            for j in range(1,len(text2)):
                if text1[i]==text2[j]:
                    dp[i][j] += max(dp[i-1][j],dp[i][j-1]) + 1
                else:
                    dp[i][j] += max(dp[i-1][j],dp[i][j-1])    

        return dp[m][n]                    
longestCommonSubsequence('abcde','ace')