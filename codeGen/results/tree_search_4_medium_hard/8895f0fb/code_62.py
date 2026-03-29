import sys

def expected_carries(N):
    dp = [0] * (N+1)
    for i in range(10, N*10+1):
        for j in range(10, min(i+1, N*10)+1):
            carry = sum((k-1) // 10 for k in range(j-9, j)) + (i-j)//10
            dp[i%N] += carry
    
    return dp[N]
