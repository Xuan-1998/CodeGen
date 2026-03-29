def min_F(a, s):
    n = len(a)
    f = 0
    for i in range(n-1):
        x = s
        y = a[i] - s
        f += x * (a[i+1] - s) + (a[i+1] - s) * (y - s)
    return f

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_F(a, s))
