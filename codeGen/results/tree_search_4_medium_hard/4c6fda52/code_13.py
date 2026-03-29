def min_changes(s, k):
    n = len(s)
    dp = [[0] * (k+1) for _ in range(n+1)]

    target = "RGB" if s[:k].count("R") > s[:k].count("G") and s[:k].count("R") > s[:k].count("B") else "BGR"

    for i in range(k):
        dp[i][0] = i

    for c in range(1, k+1):
        for i in range(c, n+1):
            min_changes = float('inf')
            for j in range(max(0, i-k), i):
                changes = dp[j][c-1] + (s[i-1] != target[c-1])
                if changes < min_changes:
                    min_changes = changes
            dp[i][c] = min_changes

    return dp[n][k]

while True:
    try:
        n, k = map(int, input().split())
        s = input()
        print(min_changes(s, k))
    except EOFError:
        break
