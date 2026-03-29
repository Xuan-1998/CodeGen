import sys

n = int(sys.stdin.readline())
costs = list(map(int, sys.stdin.readline().split()))
strings = [sys.stdin.readline().strip() for _ in range(n)]

# Sort the strings based on their length
strings.sort(key=len)

cost = 0
prev_length = len(strings[0])

for string in strings:
    if len(string) != prev_length:
        cost += min(costs)
    else:
        costs.pop(0)
        cost += costs[-1]
    prev_length = len(string)

print(cost)
