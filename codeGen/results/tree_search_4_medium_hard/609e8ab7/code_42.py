import sys
input = sys.stdin.readline

def dfs(node, l, r):
    if dp[node]:
        return dp[node]
    
    operations = float('inf')
    
    for value in range(l, r+1):
        new_operations = 0
        parent_operations = 0
        
        for ancestor in ancestors[node]:
            if value <= ancestors[ancestor]:
                new_operations += dfs(ancestor, l, value-1)
            else:
                new_operations += dfs(ancestor, value, r)
        
        operations = min(operations, new_operations + (value - l))
    
    dp[node] = operations
    return operations

n = int(input())
dp = [0]*(n+1)
ancestors = [[] for _ in range(n+1)]

for i in range(2, n+1):
    p = int(input())-1
    ancestors[i].append(p)

for i in range(1, n+1):
    l, r = map(int, input().split())
    print(dfs(i-1, l, r))
