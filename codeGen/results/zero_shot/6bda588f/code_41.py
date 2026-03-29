def min_F():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        f = 0
        for i in range(n-1):
            f += (a[i] - s) * (s if i == 0 else a[i-1] - s)
        print(f)

min_F()
