import sys
from collections import defaultdict

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        upper_rads = list(map(int, input().split()))
        lower_rads = list(map(int, input().split()))

        dp = [[0] * (C+1) for _ in range(N+1)]
        dp[0][0] = 1

        for i in range(1, N+1):
            for j in range(C+1):
                if i == 1:
                    dp[i][j] = 1
                else:
                    for k in range(min(j+1, C)+1):
                        if upper_rads.count(k) and lower_rads.count(C-k):
                            dp[i][j] += dp[i-1][k]
                            dp[i][j] %= (10**9 + 7)

        for j in range(1, C+1):
            print(dp[N][j], end=' ')
        print()

if __name__ == "__main__":
    solve()
