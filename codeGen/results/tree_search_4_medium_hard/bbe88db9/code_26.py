import sys
from collections import defaultdict

dp = defaultdict(lambda: [[sys.maxsize] * 2 for _ in range(3)])

def get_out_of_maze():
    n = int(input())
    p = list(map(int, input().split()))
    
    for i in range(n + 1):
        for x in range(3):
            dp[n+1][x][0] = 0
    
    return min(dp[n+1][x][y] for x in range(3) for y in [0, 1]) % (10**9 + 7)

print(get_out_of_maze())
