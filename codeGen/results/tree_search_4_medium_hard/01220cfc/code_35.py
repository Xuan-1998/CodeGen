    def canJump(candy):
        n = len(candy)
        dp = [False] * n
        dp[0] = True  # We can always reach index 0

        for i in range(1, n):
            for j in range(i):
                if dp[j] and i <= j + candy[j]:
                    dp[i] = True
                    break

        return dp[-1]
