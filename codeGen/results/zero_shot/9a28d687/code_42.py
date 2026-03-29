import heapq
from sys import stdin, stdout

n = int(stdin.readline())
costs = list(map(int, stdin.readsplitlines(n)))
strings = [stdin.readline().strip() for _ in range(n)]

strings.sort()

total_cost = 0
prev_string = ""

for string in strings:
    if string < prev_string:  # Current string is smaller than the previous one
        total_cost += costs[0]
    else:
        while string > prev_string:  # Need to reverse all strings from last reversed to current
            total_cost += costs[0]
    prev_string = string

print(total_cost)
