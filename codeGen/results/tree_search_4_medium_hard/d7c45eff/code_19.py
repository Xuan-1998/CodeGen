def smallest_string(n, k):
    if k > n:
        return s * ((k - 1) // n + 1)

    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if j < i:
                dp[i][j] = min(dp[i-1][j], dp[i-1][min(j-1, i-1)][-1] + s[i-1])
            else:
                dp[i][j] = dp[min(i, n)][max(0, j-n)]

    return ''.join(dp[n][k])

s = input().strip()
n = int(input())
print(smallest_string(n, k))
