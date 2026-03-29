def min_F(a, s):
    n = len(a)
    F = sum((a[i] - s) * (n - i - 1) for i in range(n))
    return F

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_F(a, s))
