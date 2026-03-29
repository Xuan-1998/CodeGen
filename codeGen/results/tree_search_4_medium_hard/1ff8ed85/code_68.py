def can_send_b(a, b):
    n = len(b)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    def dfs(i, j):
        if i > j:
            return False
        if dp[i][j]:
            return True
        if i == j:
            return b[i - 1] == a[i]
        for k in range(i, j + 1):
            if b[k - 1] == str(a[i] - a[k]) and dfs(i, k - 1) and dfs(k + 1, j):
                dp[i][j] = True
                return True
        dp[i][j] = False
        return False

    for i in range(n):
        if not dfs(0, i):
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print("YES" if can_send_b([*range(1, n + 1)], b) else "NO")
