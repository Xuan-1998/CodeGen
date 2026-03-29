import sys

def min_cost_to_sort_strings():
    n = int(sys.stdin.readline())
    costs = [int(x) for x in sys.stdin.readline().split()]
    strings = [sys.stdin.readline().strip() for _ in range(n)]

    # Sort the strings based on their lengths
    sorted_strings = sorted(strings, key=len)

    total_cost = 0
    prev_string = None

    for string in sorted_strings:
        if prev_string is not None and len(string) <= len(prev_string):
            # If the current string is shorter than or equal to the previous one,
            # we need to reverse it to get the desired lexicographical order.
            total_cost += costs[sorted_strings.index(string)]
        prev_string = string

    return total_cost

print(min_cost_to_sort_strings())
