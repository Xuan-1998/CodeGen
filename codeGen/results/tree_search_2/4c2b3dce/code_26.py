def solve():
    s = input()
    n = len(s)
    
    # Initialize the DP table
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n - 2, -1, -1):
        for j in range(i + 3, n + 1):
            if s[i:i+2] == 'AB' and s[j-2:j] == 'BA':
                dp[i][j] = True
            elif dp[i+1][j-1]:
                dp[i][j] = True
    
    print('YES' if any(all(dp[k][l]) for k in range(n)) else 'NO')

if __name__ == '__main__':
    solve()
