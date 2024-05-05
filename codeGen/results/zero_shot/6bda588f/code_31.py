def min_F(a, s):
    F = 0
    for i in range(len(a) - 1):
        if (a[i] + s) % 2 == 0:
            x_i = a[i] // 2
            y_i = a[i] // 2
        else:
            if (s < a[i]):
                y_i = s + 1
            else:
                y_i = s - 1
            x_i = a[i] - y_i
        F += x_i * y_i
    return F

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_F(a, s))
