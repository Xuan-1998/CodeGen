import sys
from collections import deque

def solve(n, k):
    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = [''] * (k+1)
    
    queue = deque([(n, 0)])
    while queue:
        i, j = queue.popleft()
        
        if j < k and i > 0: # not at the last iteration
            dp[i-1][j+1].extend(['a' + s for s in dp[i][j] if len(s) <= k-j]) 
            dp[i][j+1].extend(dp[i][j])
        
        for j in range(k+1):
            if len(''.join(dp[i][j])) > k: # the length of the string exceeds k
                break
        
    return min(dp[0][k], key=lambda x: (x, len(x)))

n, k = map(int, input().split())
print(solve(n, k))
