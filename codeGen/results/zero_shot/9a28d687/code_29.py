import sys

n = int(sys.stdin.readline())
costs = [int(sys.stdin.readline()) for _ in range(n)]
strings = [sys.stdin.readline().strip() for _ in range(n)]

# Sort strings based on their lengths and then lexicographical order
sorted_strings = sorted(strings, key=lambda s: (len(s), s))

total_cost = 0

for i in range(1, n):
    if strings[i-1] > strings[i]:
        # Strings are not in order, so we need to reverse one of them
        total_cost += min(costs[i-1], costs[i])

if sorted_strings != strings:
    print(-1)
else:
    print(total_cost)
