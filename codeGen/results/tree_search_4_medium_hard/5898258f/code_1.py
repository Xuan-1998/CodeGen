import sys

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    
    for i in range(2, N + 1):
        dp[i] = max(dp[k-1] + (A[k]-X)*bin(A[k+1]).count('1') for k in range(2, i))
    
    print(max(dp))
