import sys

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        dp = [0] * (C + 1)
        dp[0] = 1

        for i in range(1, C + 1):
            if any(u == i for u in U) and any(l == i for l in L):
                dp[i] += dp[i - 1]
            else:
                dp[i] += dp[i - 1]

        print(*dp, sep=' ')

if __name__ == '__main__':
    solve()
