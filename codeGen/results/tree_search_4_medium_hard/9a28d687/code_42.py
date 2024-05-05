import sys
from collections import defaultdict

def solve():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]
    
    max_length = 0
    for string in strings:
        max_length = max(max_length, len(string))
    
    dp = [[0] * (max_length + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, max_length + 1):
            if len(strings[i-1]) <= j:
                min_cost = float('inf')
                for k in range(j+1):
                    min_cost = min(min_cost, dp[i-1][k] + costs[i-1] * (j-k))
                dp[i][j] = min_cost
            else:
                dp[i][j] = dp[i-1][max_length]
    
    if dp[n][max_length] == float('inf'):
        print(-1)
    else:
        print(dp[n][max_length])

if __name__ == "__main__":
    solve()
