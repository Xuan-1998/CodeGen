def dfs(i, crosses):
    if i == n + 1:
        return crosses % 2
    return min(dfs(p[i] - 1, crosses) if crosses % 2 else dfs(1, crosses + 1), 
               dfs(p[i] - 1, crosses + 1) if crosses % 2 else dfs(1, crosses))

n = int(input())
p = list(map(int, input().split()))
print(dfs(1, 0))
