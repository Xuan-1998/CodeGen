import sys

def solve():
    n = int(input())
    parent = [0]*n
    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b-1] = a-1
    dp = [sys.maxsize]*n
    dp[0] = 0
    for i in range(1, n):
        parent_i = parent[i]
        while parent_i != -1:
            dp[i] = min(dp[i], dp[parent_i]+1)
            parent_i = parent[parent_i]
    res = [i+1 for i in range(n) if dp[i] == 0]
    print(len(res))
    print(' '.join(map(str, res)))

solve()
