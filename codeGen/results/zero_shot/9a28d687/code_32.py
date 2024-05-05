import sys

def min_cost_to_sort(strings):
    cost = 0
    for i in range(len(strings) - 1):
        if strings[i] > strings[i + 1]:
            cost += len(strings[i]) * 2
            strings[i], strings[i + 1] = strings[i + 1], strings[i]
    return cost

n = int(sys.stdin.readline())
costs = [int(x) for x in sys.stdin.readline().split()]
strings = [sys.stdin.readline().strip() for _ in range(n)]

# Sort the strings based on their reversed versions
strings.sort(key=lambda s: s[::-1])

# Calculate the minimum total cost required to sort the strings
min_cost = min_cost_to_sort(strings)

print(min_cost)
