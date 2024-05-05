import sys

def min_cost_to_sort_strings():
    n = int(sys.stdin.readline().strip())
    costs = list(map(int, sys.stdin.readline().split()))
    strings = [sys.stdin.readline().strip() for _ in range(n)]

    # Sort the strings based on their lengths
    sorted_strings = sorted((len(s), s) for s in strings)

    min_cost = 0
    prev_len = None

    for _, s in sorted_strings:
        if len(s) != prev_len:
            min_cost += costs[0]
        else:
            min_cost += costs[1]

        prev_len = len(s)

    return min_cost

print(min_cost_to_sort_strings())
