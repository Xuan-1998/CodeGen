def min_changes(n, k, s):
    dp = [[[0] * (k + 1) for _ in range(k + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            for c in range(k + 1):
                if s[j:j+k] == 'RGB'[c % 3] * k:
                    dp[i][j][c] = dp[i-1][0][0]
                else:
                    dp[i][j][c] = min(dp[i-1][m][n]) + 1 if s[j:j+k] in 'RGB' * (k//3) else float('inf')
    
    return dp[0][0][0]

while True:
    try:
        n, k = map(int, input().split())
        s = input()
        print(min_changes(n, k, s))
    except EOFError:
        break
