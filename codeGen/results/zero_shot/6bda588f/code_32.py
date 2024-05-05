def min_f(a, s):
    f = 0
    for ai in a:
        if ai <= s:
            f += ai * s
        else:
            f += ai * (ai - s)
    return f

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_f(a, s))
