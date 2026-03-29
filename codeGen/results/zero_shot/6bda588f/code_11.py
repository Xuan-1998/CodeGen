def min_f(a):
    n = len(a)
    if n == 1:
        return a[0] ** 2
    else:
        ans = float('inf')
        for i in range(n):
            x_i = min(s, a[i])
            y_i = max(0, a[i] - s)
            F = a[i] * (x_i + y_i) + min_f(a[1:i+1]) if i > 0 else 0
            ans = min(ans, F)
        return ans

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_f(a))
