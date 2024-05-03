code_block
n, m = map(int, input().split())
plants = list(map(int, input().split()))
coords = [list(map(float, input().split())) for _ in range(n)]

dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0

memoization = {}

def find_min_replantings(i, last_s):
    if (i, last_s) in memoization:
        return dp[i][last_s]
    
    min_replantings = float('inf')
    for s in range(m + 1):
        if plants[i - 1] == s and coords[i - 1][0] != i:
            min_replantings = min(min_replantings, find_min_replantings(i, s) + abs(coords[i - 1][0] - i))
    
    memoization[(i, last_s)] = min_replantings
    dp[i][last_s] = min_replantings
    
    return min_replantings

print(find_min_replantings(n, 0))
code_block
