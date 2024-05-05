def find_count(n):
    memo = {0: 1}
    def dp(i):
        if i not in memo:
            if i % 4 == 0 or i % 4 == 3:
                memo[i] = dp[(i-1) // 2]
            else:
                memo[i] = dp[i//2]
        return memo[i]
    return dp(n)

n = int(input())
print(find_count(n))
