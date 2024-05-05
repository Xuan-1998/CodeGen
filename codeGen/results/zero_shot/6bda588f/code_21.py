def min_product(a, s):
    n = len(a)
    total = sum(a)
    res = float('inf')
    
    for i in range(n):
        x = (total - 2 * a[i] + s) // 2 if s <= a[i] else a[i] - s
        y = a[i] - x
        res = min(res, x * y)
        
    return res

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_product(a, s))
