def check_string(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(2)]
    
    for i in range(n):
        if s[i:i+2] == 'AB':
            dp[0][i+2] = True
        elif s[i:i+2] == 'BA':
            dp[1][i+2] = True
            
        for j in range(i+3, n+1):
            if i % 2 == 0:
                dp[0][j] |= dp[0][i+2]
            else:
                dp[1][j] |= dp[1][i+2]
                
    return "YES" if (dp[0][n] or dp[1][n]) else "NO"


if __name__ == "__main__":
    s = input()
    print(check_string(s))
