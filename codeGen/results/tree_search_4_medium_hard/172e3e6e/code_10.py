from collections import defaultdict

n = int(input())
a = [int(x) for x in input().split()]

memo = defaultdict(int)
dp = {:(1, 0): 1}

for i in range(n):
    dp[(i, 0)] = memo.get((i - 1, 0), 0)
    for j in range(2, i + 1):
        if a[i] % j == 0:
            dp[(i, j - 1)] = (dp.get((j - 1, j - 2), 0) + memo.get((j - 1, j - 2), 0)) % (10**9 + 7)
    print(dp[(n, 0)])
