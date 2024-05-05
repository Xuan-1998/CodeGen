import sys
from math import comb

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, C = map(int, sys.stdin.readline().split())
        N_count = {}
        M_count = {}
        for _ in range(N):
            r = int(sys.stdin.readline())
            if r not in N_count:
                N_count[r] = 0
            N_count[r] += 1
        for _ in range(M):
            r = int(sys.stdin.readline())
            if r not in M_count:
                M_count[r] = 0
            M_count[r] += 1

        dp = [0] * (C + 1)
        dp[0] = 1
        for i in range(1, C + 1):
            for j in range(min(i, N), -1, -1):
                if i - j >= 0 and i - j <= C:
                    dp[i] += comb(N_count.get(j, 0), 1) * (dp[i - j] - dp[i - j - 1])
            for k in range(min(i, M), -1, -1):
                if i - k >= 0 and i - k <= C:
                    dp[i] += comb(M_count.get(k, 0), 1) * (dp[i - k] - dp[i - k - 1])

        print(' '.join(map(str, [dp[i] % (10**9 + 7) for i in range(1, C + 1)])))

if __name__ == "__main__":
    solve()
