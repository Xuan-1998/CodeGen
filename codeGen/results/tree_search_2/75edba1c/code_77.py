import sys

def solve(N, K, Arr):
    dp = [0] * N
    max_val = max(Arr)
    
    for i in range(1, N):
        if Arr[i] > K:
            dp[i] = 1 + sum(dp[j-1] for j in range(i+1) if max(Arr[j:i+1]) > K)
        else:
            dp[i] = dp[i-1]
    
    return sum(1 for x in dp if x > 0)

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(solve(N, K, Arr))
