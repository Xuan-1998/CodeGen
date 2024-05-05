def min_changes(s):
    n = len(s)
    k = int(input())
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    
    for i in range(k + 1):
        dp[0][i] = True
    
    count = 0
    window_start = 0
    for i in range(1, n + 1):
        if i <= k:
            dp[i][k - (i % k)] = dp[(i - 1) % k][k - ((i - 1) % k)] and s[i - 1] == "RGB"[i % 3]
        else:
            window_start = max(0, i - k)
            for j in range(k):
                if not dp[window_start + j][j]:
                    count += 1
                    break
        
    return count

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    s = input().strip()
    print(min_changes(s))
