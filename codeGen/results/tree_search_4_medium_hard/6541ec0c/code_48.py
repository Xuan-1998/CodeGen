import sys

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[[0] * (1 << 20) for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(min(i, k), 0, -1):
            for xor_val in range((1 << 20)):
                if any(a[ui] ^ a[vi] == xor_val for ui, vi in zip(range(i - 1, -1, -1), range(i)) if (ui, vi) in [(u, v) for u, v in enumerate(map(int, input().split()))]):
                    dp[i][j][xor_val] = 1
                else:
                    dp[i][j][xor_val] = max(dp[min(i - 1, j - 1)][min(j - 1, k - 1)][xor_val ^ (a[i - 1] ^ xor_val)] for _ in range(k))
    for i in range(2, n + 1):
        if any(dp[i][j][xor_val] for j in range(min(i, k) + 1) for xor_val in range((1 << 20))):
            return "YES"
    return "NO"

print(solve())
