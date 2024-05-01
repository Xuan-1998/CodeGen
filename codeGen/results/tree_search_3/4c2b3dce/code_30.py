def solve():
    n = int(input())
    s = input().strip()
    
    dp = [False] * (n + 1)
    for i in range(n - 1):
        if s[i] == 'A' and s[i+1] == 'B':
            dp[i+2] = True
        elif s[i] == 'B' and s[i+1] == 'A':
            dp[i+2] = True
    
    for i in range(n - 1, -1, -1):
        if not dp[i]:
            return "NO"
    
    return "YES"

print(solve())
