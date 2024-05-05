import sys

n, m = map(int, input().split())
dp = [[-float('inf')] * (n + 1) for _ in range(n + 1)]

curr_tail_length = 0
curr_spine_count = 0

for _ in range(m):
    u, v = map(int, input().split())
    
    if curr_tail_length > 0 and u == curr_tail_length - 1:
        curr_tail_length -= 1
        curr_spine_count -= 1
    
    dp[u][curr_spine_count] = max(dp[u][curr_spine_count], dp[v][curr_spine_count] + (curr_tail_length + 1) * (curr_spine_count + 1))
    
    if u != v:
        curr_tail_length += 1
        curr_spine_count += 1

print(max(max(row) for row in dp))

