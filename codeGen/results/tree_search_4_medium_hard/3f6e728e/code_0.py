import sys

# Define the modulus
MOD = 10**9 + 7

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        upper_radii = list(map(int, input().split()))
        lower_radii = list(map(int, input().split()))

        dp = [0] * (C + 1)
        dp[0] = 1

        for i in range(1, C + 1):
            for j in range(N):
                if upper_radii[j] >= i:
                    dp[i] += dp[i - 1]
                    dp[i] %= MOD
            for k in range(M):
                if lower_radii[k] >= i:
                    dp[i] += dp[i - 1]
                    dp[i] %= MOD

        print(*dp, sep=' ')

if __name__ == '__main__':
    solve()
