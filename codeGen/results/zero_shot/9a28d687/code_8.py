import sys
from io import StringIO

input_str = sys.stdin.read()
input_str += "\n"  # add a newline at the end to simplify reading

strings = input_str.split("\n")[2:]  # split by newline and skip the first two lines (n and costs)
costs = list(map(int, input_str.split("\n")[1].split()))  # split by newline and convert to int

sorted_strings = []

for s in strings:
    rev_s = s[::-1]  # reverse each string
    sorted_strings.append(rev_s)

sorted_strings.sort()  # sort the reversed strings lexicographically

total_cost = 0

for i in range(len(sorted_strings)):
    total_cost += costs[strings.index(sorted_strings[i])]

if sorted_strings != strings:
    print(-1)
else:
    print(total_cost)
