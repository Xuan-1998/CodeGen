from collections import deque

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_val = max(arr)
    min_val = min(arr)
    
    dp = [[False] * (max_val + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    queue = deque([(0, 0)])
    
    while queue:
        i, k = queue.popleft()
        
        if i == n:
            return "YES"
        
        for j in range(1, n - i + 1):
            new_k = abs(k - arr[i + j])
            dp[i + j][new_k] = (dp[i + j][new_k]) or ((k > 0) == (arr[i + j] >= k))
            queue.append((i + j, new_k))
    
    return "NO"

print(solve())
