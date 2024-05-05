import sys

def min_cost_sort(strings):
    # Sort the strings based on their lengths and costs
    strings.sort(key=lambda x: (len(x), cost[x]))

    total_cost = 0
    prev_string = None

    for string in strings:
        if prev_string is not None and string < prev_string:
            # Reversing the current string will make it smaller than the previous one
            total_cost += cost[string]
        elif prev_string is not None and string > prev_string:
            # We need to reverse the previous string to make it larger than the current one
            total_cost += cost[prev_string] + cost[string]
        else:
            # The strings are already in order, so we don't need any reversals
            pass

        prev_string = string

    return total_cost

# Read input from stdin
n = int(sys.stdin.readline())
cost = {}
strings = []

for i in range(n):
    c = int(sys.stdin.readline())
    cost[i+1] = c
    strings.append(input())

# Calculate and print the minimum total cost
print(min_cost_sort(strings))
