import sys

mod = 10**9 + 7

def solve():
    dp = [0] * (C + 1)
    dp[0] = 1

    for i in range(1, C + 1):
        for r in range(min(i, N), -1, -1):  # Update upper hemispheres
            dp[i] += dp[r]
            dp[i] %= mod
        for r in range(min(i, M), -1, -1):  # Update lower hemispheres
            dp[i] = (dp[i] + dp[r]) % mod

    return ' '.join(map(str, dp))  # Convert list to string and join with spaces

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        print(solve())
