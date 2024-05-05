code
def find_smallest_string():
    n, k = map(int, input().split())
    s = input()

    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, min(i+1, k)+1):
            if j <= i:
                dp[i][j] = min(dp[i-1][j], [s[:i-1]] + dp[i-1][j-1]) if s[i-1] != '' else s[:i]
            elif j > i and j % (i+1) == 0:
                dp[i][j] = dp[i//2][i//2]*(k//i) + s[:k%i]

    return ''.join(dp[n][k])

print(find_smallest_string())
code
