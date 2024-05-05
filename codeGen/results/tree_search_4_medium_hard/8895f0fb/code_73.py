import sys

def calculate_carries(N):
    dp = [0] * (N + 1)
    
    for i in range(2, N + 1):
        if i == 2:
            dp[i] = 6
        else:
            dp[i] = (dp[i - 1] + 2 * dp[i - 1]) / (i + 1)
    
    return dp[N]

T = int(input())
for _ in range(T):
    N = int(input())
    print(calculate_carries(N))
