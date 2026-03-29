import sys
from collections import deque

def min_operations():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[0] * (10001) for _ in range(n + 1)]
    prev = [-1] * (n + 1)
    
    queue = deque([(0, 0)])
    
    while queue:
        i, j = queue.popleft()
        
        if i > 0 and dp[i][j] == dp[i - 1][prev[i]]:
            continue
        
        for k in range(j):
            if arr[k] < arr[j]:
                new_ops = (k + arr[j]) // arr[k]
                if new_ops > dp[i - 1][k]:
                    queue.append((i, j))
                    dp[i][j] = new_ops
                    prev[i] = k
                break
    
    return sum(dp[-1])

print(min_operations())
