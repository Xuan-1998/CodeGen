import sys; input = sys.stdin.readline

a, b = map(int, input().split())
n, m = a.bit_length(), b.bit_length()
dp = [[0] * (m + 1) for _ in range(n + 1)]

memo = {}
def solve(i, j):
    if (i, j) in memo:
        return memo[(i, j)]
    if i == 0 and j == 0:
        return 0
    res = dp[i-1][j-1] if i > 0 and j > 0 else 0
    if i % 2 == 0 and j % 2 == 0:
        memo[(i, j)] = solve(i // 2, j // 2)
    elif i % 2 == 0 or j % 2 == 0:
        res += 1
    return (res + solve((i - 1) // 2 if i % 2 == 0 else i - 1, (j - 1) // 2 if j % 2 == 0 else j - 1)) % (10**9 + 7)

print(solve(n, m))
