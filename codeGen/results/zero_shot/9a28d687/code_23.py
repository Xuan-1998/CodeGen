def min_cost_to_sort_strings():
    n = int(input())  # Read the number of strings from stdin
    costs = list(map(int, input().split()))  # Read the cost associated with each string
    strings = [input() for _ in range(n)]  # Read the strings

    sorted_strings = [''] * n  # Initialize an array to store the sorted strings
    total_cost = 0  # Initialize the total cost to 0

    for i in range(len(strings)):
        while not all(sorted_strings[:i] <= s and (s == '' or all(t <= s for t in strings[:i])) for s in strings[i:]):
            j = min(range(i, len(strings)), key=lambda x: sum(c if strings[x][::-1] < strings[y] else 0 for y in range(x)))
            total_cost += costs[j]
            sorted_strings[j], strings[j] = strings[j][::-1], ''

    return -1 if any(len(s) > 0 for s in strings) else total_cost

print(min_cost_to_sort_strings())
