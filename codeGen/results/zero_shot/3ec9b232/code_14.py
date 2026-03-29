import sys
from collections import defaultdict

# Read input
n = int(input())
M = list(map(int, input().split()))

# Step 1: Count the frequency of each element in M
freq = defaultdict(int)
for x in M:
    freq[x] += 1

# Step 2: Calculate the number of ways to create V for each element in M
V = [0] * (n + 1)
for i, m in enumerate(M):
    for j in range(n, m - 1, -1):
        V[j] += freq[m]

# Step 3: Calculate the total number of different ways to create V
total_ways = 1
for v in V:
    total_ways = (total_ways * (v + 1)) % (10**9 + 7)

print(total_ways)
