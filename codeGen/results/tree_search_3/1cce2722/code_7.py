import sys

def solve():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]

    memo = {}

    def dp(i, k):
        if (i, k) in memo:
            return memo[(i, k)]

        if i == 0:
            return 0

        if k not in a[:i]:
            return dp(i - 1, k)

        max_points = dp(i - 1, k)
        for j in range(i):
            if a[j] == k + 1 or a[j] == k - 1:
                max_points = max(max_points, dp(j, a[j]) + 1)

        memo[(i, k)] = max_points
        return max_points

    print(dp(n, a[0]))

solve()
