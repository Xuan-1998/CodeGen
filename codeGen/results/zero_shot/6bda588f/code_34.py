def min_f(a):
    n = len(a)
    res = 0
    for i in range(n):
        if a[i] >= 2*s:
            res += (a[i]-s) * s
        else:
            res += s * s
    return res

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_f(a))
