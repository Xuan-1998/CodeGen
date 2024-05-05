def min_cost(strings):
    # Sort the strings based on their cost
    sorted_strings = sorted(zip([cost for _, cost in strings], _), key=lambda x: x[0])

    min_total_cost = 0

    for i in range(len(sorted_strings) - 1):
        if len(sorted_strings[i][1]) > len(sorted_strings[i + 1][1]):
            # If the current string is longer than its successor, we need to reverse it
            min_total_cost += sorted_strings[i][0]

    return min_total_cost if min_total_cost == 0 else -1

# Read input and call the function
n = int(input())
strings = [input().strip() for _ in range(n)]

print(min_cost([(len(s), s) for s in strings]))
