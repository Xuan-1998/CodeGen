t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    
    min_f = float('inf')
    for i in range(n-1):
        x = (a[i] - s) // 2
        y = a[i] - x
        
        f = x * y + (y if i < n-2 else 0)
        min_f = min(min_f, f)
    
    print(min_f)
