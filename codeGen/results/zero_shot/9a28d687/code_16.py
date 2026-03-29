# Step 1: Read input
n = int(input())  # number of strings
costs = list(map(int, input().split()))  # costs for reversing each string
strings = [input() for _ in range(n)]  # read all strings

# Step 2: Sort the strings by their lexicographical order
sorted_strings = sorted(strings)

# Step 3: Calculate the minimum total cost required to sort the strings in lexicographical order
total_cost = 0
for i in range(len(sorted_strings)):
    while not is_sorted(sorted_strings, costs):
        # Reverse a string if necessary to maintain lexicographical order
        reverse_index = find_reverse_index(sorted_strings, costs)
        sorted_strings[reverse_index] = strings[reverse_index][::-1]
        total_cost += costs[reverse_index]
    break  # If the strings are already in lexicographical order, no further reversals needed

# Step 4: Output the minimum total cost
print(total_cost)

def is_sorted(strings, costs):
    for i in range(len(strings) - 1):
        if strings[i] > strings[i + 1]:
            return False
    return True

def find_reverse_index(sorted_strings, costs):
    for i in range(len(sorted_strings)):
        if sorted_strings[i][::-1] < sorted_strings[i]:
            return i
    return -1  # If no string needs to be reversed, return -1
