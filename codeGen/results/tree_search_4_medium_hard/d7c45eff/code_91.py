def min_string(n, k):
    s = input().strip()
    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            if i == 0 or j == 0:
                dp[i][j] = [''] * j
            else:
                last_char = s[i-1]
                if not dp[i-1][j]:
                    dp[i][j] = [last_char + c for c in dp[i-1][j-1]]
                else:
                    min_str = min(dp[i-1][j])
                    if last_char < min_str[0]:
                        dp[i][j] = [last_char + c for c in dp[i-1][j-1]]
                    else:
                        dp[i][j] = [c for c in dp[i-1][j] if c != min_str]
    
    return ''.join(min(dp[n][k], key=lambda x: (x, len(x))))
