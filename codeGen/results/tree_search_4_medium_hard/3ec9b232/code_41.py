import sys; sys.setrecursionlimit(10000)
def merge_sort_ways(n):
    MOD = 10**9 + 7
    dp = [[0]*(n) for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            for k in range(i, j+1):
                if k == i:
                    dp[i][j] += dp[i][k-1]
                else:
                    dp[i][j] += dp[k-1][j]
                dp[i][j] %= MOD
    return dp[0][n-1]

# read input from standard input
n = int(input())
m = list(map(int, input().split()))

# print the answer to standard output
print(merge_sort_ways(n))
