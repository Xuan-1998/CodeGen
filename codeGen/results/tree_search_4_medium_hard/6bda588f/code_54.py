def dp(n, s):
    if n == 1:
        return a[n-1]
    min_F = float('inf')
    for x in range(s+1):
        y = a[n-1] - x
        if (x-s)*(y-s) >= 0:
            F = x*y + dp(n-1, s)
            min_F = min(min_F, F)
    return min_F

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(dp(n, s))
