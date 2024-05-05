import sys
from operator import itemgetter

n = int(sys.stdin.readline())
costs = [int(c) for c in sys.stdin.readline().split()]
strings = [sys.stdin.readline().strip() for _ in range(n)]

def reverse_key(s):
    return s[::-1]

sorted_strings = sorted(zip(costs, strings), key=reverse_key)

total_cost = 0
prev_s = None

for c, s in sorted_strings:
    if prev_s is not None and s < prev_s:
        total_cost += c
    prev_s = s

print(total_cost)
