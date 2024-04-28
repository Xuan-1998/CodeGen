import sys; input = lambda: sys.stdin.readline().strip(); flush = lambda: [input() for _ in range(int(input()))]

n, m = map(int, input().split())
edges = [(int(input()), int(input())) for _ in range(m)]

k = int(input()); path = list(map(int, input().split()))
path_dict = {i+1:i for i in path}

dp = [0] * (n + 1)

pq = []

for i in range(1, k):
    j = path_dict[path[i - 1]]
    dp[path[i]] = min(dp[j] + 1, i)
    pq.append((dp[path[i]], path[i]))

pq.sort()

min_recomputation = pq[0][0]; max_recomputation = pq[-1][0]

print(min_recomputation, max_recomputation)
