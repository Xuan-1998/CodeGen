def mergeable(p):
    n = len(p) // 2
    dp = [[["NO"] for _ in range(2 * n + 1)] for _ in range(n)]

    def dfs(i, a, b):
        if i > n:
            return "YES"
        if dp[i][a][b] != ["NO"]:
            return eval(dp[i][a][b])

        if i == n:
            return "YES" if p[:i] == list(range(a, 2 * n)) or p[:i] == list(range(b, 2 * n)) else "NO"

        if a < b:
            res = dfs(i + 1, a + 1, b)
            if not res and i < n:
                res = dfs(i + 1, a, b + 1)
            return ["YES" if res else "NO"]
        else:
            res = dfs(i + 1, a - 1, b)
            if not res and i < n:
                res = dfs(i + 1, a, b + 1)
            return ["YES" if res else "NO"]

    return "YES" if dfs(0, 0, 0) else "NO"

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        print("YES" if mergeable(p) else "NO")

if __name__ == "__main__":
    main()
