import sys
from collections import Counter

# Read input
n = int(input())
m = list(map(int, input().split()))

# Initialize variables
total_ways = 0
count_map = Counter(m)

for m_i in count_map:
    for j in range(count_map[m_i]):
        # Calculate ways for this number
        if m_i == n:
            ways = 1
        else:
            ways = (m_i + 1) * pow(2, n - m_i - 1, 10**9+7)
        total_ways += ways

print(total_ways % (10**9+7))
