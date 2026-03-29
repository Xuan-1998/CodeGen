import math
MOD = 998244353

def solve():
    n = int(input())
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # base cases
    for i in range(n + 1):
        dp[i][i] = 1
    
    # fill up the dp table
    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            for cut_index in range(left, right):
                dp[left][right] += dp[left][cut_index] * dp[cut_index + 1][right]
                dp[left][right] %= MOD
    
    # count the good permutations
    good_permutations = 0
    for left in range(n - 1):
        for right in range(left, n):
            if (left + 1) % (right - left + 2) == 0:
                good_permutations += dp[0][left] * dp[left + 1][right]
                good_permutations %= MOD
    
    return good_permutations
