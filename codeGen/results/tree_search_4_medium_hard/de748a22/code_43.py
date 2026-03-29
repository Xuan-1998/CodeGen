from collections import defaultdict

def solve():
    n, q = map(int, input().split())
    signs = [1 if x == "+" else -1 for x in input()]
    queries = [list(map(int, input().split())) for _ in range(q)]

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    bit = defaultdict(int)

    def update(x):
        while x <= n:
            bit[x] += 1
            x += x & -x

    def query(x):
        result = 0
        while x > 0:
            result += bit[x]
            x -= x & -x
        return result

    for i in range(n):
        dp[i][i] = signs[i]

    for length in range(1, n):
        for left in range(n - length):
            right = left + length
            if signs[left] != signs[right]:
                dp[left][right] = 0
            else:
                dp[left][right] = dp[left][left] + dp[right][right]

    for l, r in queries:
        sign_sum = query(r) - query(l - 1)
        print(min(sign_sum, abs(sign_sum)))

solve()
