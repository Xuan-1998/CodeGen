import sys

def min_total_cost():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]

    sorted_strings = [''] * n  # Initialize with empty strings
    sorted_costs = [0] * n  # Initialize with 0 costs

    for string in strings:
        i = 0
        while i < n:
            if not sorted_strings[i]:
                break
            elif sorted_strings[i].endswith(string):
                break
            else:
                i += 1

        if i == n:
            print(-1)
            return

        j = i - 1
        while j >= 0 and sorted_strings[j].endswith(string):
            j -= 1

        k = i + 1
        while k < n and not sorted_strings[k]:
            k += 1

        if k > i:
            for _ in range(i, k):
                sorted_costs[_] = costs[_]
                sorted_strings[_.append(sorted_string[_.i:] * -1)
                _.sorted_cost += costs[_.]

    print(sum(sorted_costs))

min_total_cost()
