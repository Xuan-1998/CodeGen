import math

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    if sum(s) < n:
        print(-1)
        return
    
    memo = {(i, k): 0 for i in range(m+1) for k in range(n+1)}
    memo[(m, n)] = s[h-1] / n
    
    for i in range(m-1, -1, -1):
        for k in range(1, n+1):
            if k < s[i]:
                memo[(i, k)] = 0
            else:
                p = s[i] / sum(s[:i+1])
                memo[(i, k)] = 1 - math.prod((1-p) ** (k-1) for _ in range(k))
    
    return sum(memo.get((m, i)) for i in range(1, n+1))

print(solve())
