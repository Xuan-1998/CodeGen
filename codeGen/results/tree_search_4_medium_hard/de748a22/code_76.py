code = '''
def solve(n, q):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    sign = [int(c) for c in input()]
    for i in range(1, n + 1):
        if sign[i - 1] == sign[i - 2]:
            dp[i - 1][i] += 1
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            if sign[r - 1] == sign[l - 1]:
                dp[l][r] = min(dp[l][l], dp[l][r - 1]) + 1
    res = []
    for _ in range(q):
        l, r = map(int, input().split())
        print(min(dp[l][r], dp[l-1][r-1]))
'''

print(code)
