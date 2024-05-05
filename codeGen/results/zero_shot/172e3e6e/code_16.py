import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Initialize dp array with zeros
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(n):
        for j in range(i+1, n+1):
            if a[i-1] % j == 0:
                dp[j] += dp[i]
                dp[j] %= 10**9 + 7
                
    return sum(dp)

print(solve())
