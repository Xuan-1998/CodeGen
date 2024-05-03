import sys
from functools import lru_cache

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        A = [list(map(int, input().split())) for _ in range(n)]
        dp = [0] * (n + 1)
        dp[0] = 1
        @lru_cache(None)
        def dfs(i, prev):
            if i > n:
                return 1
            p = 1
            for a, b in A[i:]:
                if a != b and (a not in prev or b not in prev):
                    p *= (1 - min(A[i][0], A[i][2]) / 100)
                elif a not in prev:
                    p *= A[i][0] / 100
                elif b not in prev:
                    p *= A[i][2] / 100
            return p
        ans = 0
        for i in range(n):
            if A[i][0] != A[i][1]:
                dp[i + 1] += dfs(i, set(A[i]))
        print(f"{dp[-1]:.6f}")

if __name__ == "__main__":
    solve()
