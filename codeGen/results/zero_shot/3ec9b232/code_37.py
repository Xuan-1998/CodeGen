import sys

def solve():
    n = int(input())
    M = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n):
        if M[i] > M[i - 1]:
            dp[i] += dp[i - 1]
        if i >= 2 and M[i] <= M[i - 1] and M[i] <= M[i - 2]:
            dp[i] += dp[i - 1] * (i - 1)
    
    print(dp[-1] % (10**9 + 7))

if __name__ == "__main__":
    solve()
