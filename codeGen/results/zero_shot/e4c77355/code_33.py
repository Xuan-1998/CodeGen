import sys

def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

print(solve())
