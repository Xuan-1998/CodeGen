from collections import defaultdict

def min_f(n, s, a):
    dp = defaultdict(int)
    for i in range(2, n+1):
        for x in range(i):
            y = i - x - 1
            if (x - s) * (y - s) >= 0:
                dp[(i, x + y)] = min(dp.get((i-1, x-y+s), float('inf')) + a[i-1] - s, dp[(i-1, x+y-s)] + a[i-1])
    return dp.get((n, a[n-1]), float('inf'))

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_f(n, s, a))
