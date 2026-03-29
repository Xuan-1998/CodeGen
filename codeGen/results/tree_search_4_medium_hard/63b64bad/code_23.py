import sys
from collections import defaultdict

def simulate_program(a, n):
    memo = defaultdict(int)
    flag = False
    
    def dfs(x, y):
        nonlocal flag
        if (x, y) in memo:
            return memo[(x, y)]
        
        if x > n or x <= 0:
            flag = True
        
        if not flag:
            memo[(x, y)] = max(dfs(x+a[x-1], y+a[x-1]), dfs(x-a[x-1]+a[x-1], y+a[x-1]))
        
        return memo[(x, y)]

    dfs(1, 0)
    
    if flag:
        return -1
    else:
        return memo[(1, 0)]


n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    print(simulate_program(a, n))
