def minF(n, s, a):
    f = [0] * (n + 1)
    
    for i in range(2, n + 1):
        x, y = divmod(a[i - 1], s)
        
        if x > y:
            f[i] = min(f[i - 1], (x - s) * a[i - 1])
        else:
            f[i] = min(f[i - 1], (y - s) * a[i - 1])
    
    return f[n]

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(minF(n, s, a))
