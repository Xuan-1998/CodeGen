def solve():
    s = input()
    dp = [False] * (len(s) + 1)
    
    for i in range(2, len(s) + 1):
        if (s[i-1] == 'A' and s[i-2] == 'B') or (s[i-1] == 'B' and s[i-2] == 'A'):
            dp[i] = True
        elif i >= 3:
            dp[i] = dp[i-3] and ((s[i-1] == 'A' and s[i-2] == 'B') or (s[i-1] == 'B' and s[i-2] == 'A'))
    
    result = False
    for i in range(len(s)):
        if dp[i]:
            result = True
            break
    
    print("YES" if result else "NO")

solve()
