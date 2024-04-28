def solve():
    s = input().strip()
    n = len(s)
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(i, n):
            if s[i:i+2] == 'AB' and s[j-1:j+1] == 'BA':
                dp[i][j] = 1
            elif (s[i:i+2] == 'AB' or s[i:i+2] == 'BA') and i + 2 <= j:
                dp[i][j] = 1 if dp[i+2][j] else 0
                
    print('YES' if any(dp[i][n-1] for i in range(n)) else 'NO')

if __name__ == '__main__':
    solve()
