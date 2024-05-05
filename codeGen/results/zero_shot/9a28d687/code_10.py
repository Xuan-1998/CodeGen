# Read input
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

# Sort strings based on their lexicographical order and minimum cost to reverse
sorted_strings = sorted((string, sum(cost if string[i] != s else 0 for i, (s, c) in enumerate(zip(strings[0], costs))), 0), key=lambda x: (x[0], x[1]))

# Check if all strings are the same or not
all_same_string = len(set(strings)) == 1

# Calculate total cost if all strings are the same
total_cost_same = sum(costs) * n

# If all strings are the same, return total cost
if all_same_string:
    print(total_cost_same)
else:
    # Calculate total cost by reversing strings to sort them lexicographically
    total_cost = 0
    for i in range(1, n):
        while sorted_strings[i][0] < sorted_strings[i-1][0]:
            total_cost += sorted_strings[i][1]
            sorted_strings[i] = (sorted_strings[i][0][::-1], *sorted_strings[i][1:])
    print(total_cost)
