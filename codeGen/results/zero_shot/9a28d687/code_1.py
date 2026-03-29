n = int(input())  # number of strings
costs = [int(input()) for _ in range(n)]  # cost of reversing each string
strings = [input() for _ in range(n)]  # the strings themselves

sorted_strings = sorted(strings, key=lambda x: (len(x), x))

total_cost = 0
for i in range(1, n):
    if len(sorted_strings[i]) > len(sorted_strings[i-1]):
        total_cost += costs[i]
    elif strings[i] < strings[i-1]:
        total_cost += costs[i]

print(total_cost)
