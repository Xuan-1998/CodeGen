import sys

def solve():
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(m + 1):
            if j < m:
                u, v = map(int, input().split())
                p = set(range(u, v + 1))
                
                # If the current vertex is not included in the tail
                if i not in p:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + 1)
                else:  
                    # The length of the new spine and the beauty so far
                    new_beauty = j + 1
                    if i in p:
                        p.remove(i)
                    dp[i][j] = max(dp[i - 1][j], new_beauty * len(p))
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][m]

print(solve())
