from collections import defaultdict

def memoize(func):
    memo = defaultdict(int)
    def wrapper(prev_color, i):
        key = (prev_color, i)
        if key in memo:
            return memo[key]
        result = func(prev_color, i)
        memo[key] = result
        return result
    return wrapper

@memoize
def min_recolor(prev_color, i):
    if i == 0: return 0
    dp = [[float('inf')] * 3 for _ in range(i+1)]
    dp[0][0], dp[0][1], dp[0][2] = 0, 0, 0

    for j in range(1, i+1):
        for c in [0, 1, 2]:
            if prev_color != c:
                dp[j][c] = min(dp[j-1][k]) + (1 if c == 0 else 0) + (1 if c == 1 else 0)
            else:
                dp[j][c] = dp[j-1][c]
    return min(dp[-1])

n, s = map(int, input().split())
s = list(s)

r = min_recolor(3, n-1)
print(r)

ans = [0]*n
prev_color = 3
for i in range(n):
    if prev_color == 3: color = 2
    elif prev_color == 2: color = 1
    else: color = 0
    ans[i] = 'RGB'[color]
    prev_color = color
print(''.join(ans))
