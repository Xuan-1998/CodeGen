def merge_arrays(p):
    n = len(p) // 2
    dp = [[False] * (n + 1) for _ in range(2 * n + 1)]

    def dfs(i, j):
        if i - j > n:
            return False
        if i - j == n:
            return True
        if dp[i][j]:
            return True

        for k in range(n, 0, -1):
            if (i - k) % 2 == 0 and dfs(i - k, j + k):
                return True
            if (i - k) % 2 != 0 and dfs(i - k - 1, j + k - 1):
                return True

        return False

    for i in range(n, 2 * n):
        for j in range(0, n + 1):
            if not dfs(i, j):
                print("NO")
                return
    print("YES")

n = int(input())
p = list(map(int, input().split()))
merge_arrays(p)
