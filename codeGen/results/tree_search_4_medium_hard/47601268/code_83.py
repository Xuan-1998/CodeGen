from sys import stdin

def solve(n):
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[0][i] = True
    
    for k in range(1, n + 1):
        for i in range(k, n + 1):
            if (i % 2 == 0 and k > 0) or not dp[k-1][i//2]:
                dp[k][i] = True
            else:
                dp[k][i] = dp[k][i // 2]
    
    count = 0
    for i in range(n + 1):
        if dp[0][i]: 
            count += 1
    
    return count

n = int(stdin.readline())
print(solve(n))
