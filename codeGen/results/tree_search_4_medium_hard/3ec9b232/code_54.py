from collections import defaultdict

def solve():
    n = int(input())
    m = list(map(int, input().split()))
    
    dp = defaultdict(int)
    dp[(0, 0)] = 1
    
    for i in range(1, n):
        for j in range(i + 1):
            if m[i - 1] < i:
                dp[(i, j)] += dp[(m[i - 1], j)]
            else:
                dp[(i, j)] += dp[(m[i - 1], j)]
    
    print((dp[(n, 0)] % (10**9 + 7)) if n > 0 else 0)
