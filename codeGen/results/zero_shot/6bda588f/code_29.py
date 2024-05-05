import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    min_f = 0
    for i in range(n):
        if a[i] <= s:
            x = y = a[i] // 2
        else:
            x = s
            y = a[i] - s
        min_f += x * y
    print(min_f)
