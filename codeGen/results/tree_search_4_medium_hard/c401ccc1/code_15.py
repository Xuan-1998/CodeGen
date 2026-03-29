import sys
from collections import defaultdict

q = int(input())

# Create a hashmap for each vertex to store its neighbors
graph = defaultdict(list)
for _ in range(q):
    u, v = map(int, input().split())
    graph[u].append(v)

dp = [[False] * 2**30 for _ in range(2**30)]

for i in range(2**30):
    dp[i][i] = False

for u in range(2**30):
    for w in range(2**30):
        if (u & w) == w:
            for k in range(20):
                bit_set = 1 << k
                if (w & bit_set) and not dp[u][w]:
                    dp[w][w | bit_set] = True

for _ in range(q):
    u, v = map(int, input().split())
    print("YES" if dp[u][v] else "NO")
