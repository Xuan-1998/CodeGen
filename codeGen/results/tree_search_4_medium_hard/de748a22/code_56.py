def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    def recursive_remove(i, j):
        if i < l or i >= r:
            return 0
        if signs[i] == signs[j]:
            return dp[i][j]
        min_remove = float('inf')
        for k in range(i, j):
            if signs[k] != signs[i]:
                remove = recursive_remove(i, k) + 1
                min_remove = min(min_remove, remove)
        dp[i][j] = min_remove
        return min_remove

    for _ in range(q):
        l, r = map(int, input().split())
        print(recursive_remove(0, r - 1))

if __name__ == "__main__":
    solve()
