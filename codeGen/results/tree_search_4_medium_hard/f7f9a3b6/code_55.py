def solve():
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]

    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    ways = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, n // a[s[i - 1] - 97] + 2)):
            dp[i][j] = min((j - 1) + (s[:i].count(c) // a[c - 97] + 1 if s[:i].count(c) % a[c - 97] > 0 else 0 for c in set(s[:i]))[0], j) + 1
            ways[i][j] = dp[i][j]

    print(dp[n][n // max(a)])
    print(max(len(s[:i]) for i in range(n + 1)))
    print(min(way for way, _ in ways))

if __name__ == "__main__":
    solve()
