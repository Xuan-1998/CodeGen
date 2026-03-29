import sys

def min_operations():
    N = int(input())
    A = list(map(int, input().split()))

    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = min(dp[i], dp[j - 1] + abs(A[i] - A[j]))
    
    return dp[-1]

print(min_operations())
