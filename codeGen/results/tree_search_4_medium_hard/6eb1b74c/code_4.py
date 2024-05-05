import sys

def solve():
    t = input().strip()
    n = int(input())
    strings = [input() for _ in range(n)]

    dp = [[[0] * (n + 1) for _ in range(len(t) + 1)] for _ in range(len(t) + 1)]
    md = {}

    for i in range(1, len(t) + 1):
        for j in range(i):
            if t[j:i] in strings:
                dp[i][j][n] = min(dp[i][j][n], dp[j][j][n] + 1)
                md[(i, n)] = (j, i)

    m = dp[-1][-1][-1]
    res = []

    for _ in range(m):
        j, k = md.popitem()[1]
        res.append((k - j + 1, k))

    print(-1 if m == 0 else m)
    for p, w in sorted(res, reverse=True):
        print(f"({w}, {p})")

if __name__ == "__main__":
    solve()
