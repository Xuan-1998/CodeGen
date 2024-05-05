import sys

def adjust_tree_values():
    n = int(input())
    parent = list(map(int, input().split()))
    ranges = [list(map(int, input().split())) for _ in range(n-1)]

    dp = [[0] * (ranges[i][1] - ranges[i][0] + 1) for i in range(n)]
    
    for i in range(2, n):
        l, r = ranges[parent[i-1]]
        for j in range(l, r+1):
            dp[i][j-l] = min(dp[i][j-l], dp[parent[i-1]][k] + (0 if k == 0 else 1) for k in range(j-l+1))
    
    res = sum(max(min(dp[i]) for i in range(2, n)) - i for i in range(2, n))
    
    return res

print(adjust_tree_values())
