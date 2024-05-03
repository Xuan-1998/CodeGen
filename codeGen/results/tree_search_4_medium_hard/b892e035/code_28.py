import sys

def probability(n, probabilities):
    dp = [[0] * (n + 1) for _ in range(17)]
    dp[0][n] = 1
    
    for i in range(n):
        p1, a1, b1 = map(float, input().split())
        p2, a2, b2 = map(float, input().split())
        
        for j in range(min(a1, a2) + 1, max(b1, b2) + 1):
            dp[j][n - i - 1] += dp[j-1][n-i]*(p1*(b1-j+1)*(j-a1+1)+p2*(b2-j+1)*(j-a2+1))
    
    return round(dp[16][0], 6)

T = int(input())
for _ in range(T):
    n = int(input())
    print(probability(n, None))
