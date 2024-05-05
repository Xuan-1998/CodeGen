import sys
from collections import defaultdict

def calculate_max_profit(n, m, c0, d0):
    dp = {(i, j) for i in range(n+1) for j in range(m+1)}
    memo = defaultdict(int)

    def dfs(dough_left, available_stuffs):
        if (dough_left, available_stuffs) not in memo:
            if dough_left < c0:
                result = 0
            else:
                result = max(result + d0 - (c0-dough_left), 
                              sum(max(0, ai-bi+d0-ci) for _,ai,bi,ci in [(d0,c0,d0,d0)] + list(zip(*[map(int,line.split()) for line in [line.strip() for line in sys.stdin]][1:]))) 
            memo[(dough_left, available_stuffs)] = result
        return memo[(dough_left, available_stuffs)]

    print(dfs(c0, m))

# Read input from standard input
n, m, c0, d0 = map(int, [line.strip() for line in sys.stdin][0].split())
print(n,m,c0,d0)
[ai, bi, ci, di] = [list(map(int, line.split())) for line in [line.strip() for line in sys.stdin][1:]]
