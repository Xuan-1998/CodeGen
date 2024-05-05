def min_cuts(s):
    n = len(s)
    dp = [[False] * (n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][i] = True
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = (length == 2) or dp[i+1][j-1]
            else:
                dp[i][j] = False
    
    cuts = 0
    for i in range(n):
        if not dp[0][i]:
            cuts += 1

    return cuts

n = int(input())
s = input()
print(min_cuts(s))
