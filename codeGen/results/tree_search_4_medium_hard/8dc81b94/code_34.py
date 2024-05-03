def can_make_zero():
    n = int(input())
    a = list(map(int, input().split()))
    dp = {}
    
    for i in range(n):
        for k in range(1000001):
            if i == 0:
                dp[(i, k)] = (k == 0)
            elif not dp.get((i-1, max(0, min(a[i], k)))) and not dp.get((i-1, min(max(0, k-a[i]), 10**6))):
                dp[(i, k)] = False
            else:
                dp[(i, k)] = (dp.get((i-1, max(0, min(a[i], k))))) or (dp.get((i-1, min(max(0, k-a[i]), 10**6)))))
    
    for i in range(n):
        if not any(dp.get((i, j)) for j in range(1000001)):
            return "NO"
    return "YES"

print(can_make_zero())
