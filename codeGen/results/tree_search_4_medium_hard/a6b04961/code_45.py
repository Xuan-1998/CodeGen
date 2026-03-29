from collections import defaultdict

n, m = map(int, input().split())
dp = defaultdict(int)

for i in range(n + 1):
    for j in range(m + 1):
        if i > 0 and j > 0:
            dp[(i, j)] = max(dp.get((i - 1, j), 0) * (j + 1), dp.get((i, j - 1), 0))
        else:
            dp[(i, j)] = 0 if i == 0 or j == 0 else i

print(dp.get((n, m), 0))
