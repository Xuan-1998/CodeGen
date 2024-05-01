from sys import stdin

def solve():
    n = int(stdin.readline())
    s = [int(x) for x in stdin.readline().split()]
    
    dp = [[False] * (1 << n) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for k in range((1 << i) - 1, -1, -1):
            if any(dp[i-1][l] and not (s[i-1] & (1 << l)) for l in range(n)):
                dp[i][k | (1 << i)] = True
    
    return [i for i in range((1 << n) - 1, -1, -1) if dp[n][i]]

print(*solve(), sep='\n')
