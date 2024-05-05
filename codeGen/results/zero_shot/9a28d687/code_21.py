python
# Step 1: Read the input
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

# Step 2: Sort the strings based on their lengths. This is because we can only reverse strings to sort them.
sorted_strings = sorted(strings, key=len)

# Step 3: Initialize the minimum cost and the current string index
min_cost = 0
current_index = 0

# Step 4: Iterate through the sorted strings
for i in range(n):
    # Find the first string that is not equal to the current string
    while current_index < n:
        if strings[current_index] != sorted_strings[i]:
            break
        current_index += 1
    
    # If we could not find a different string, it means the strings are already sorted and we can stop here
    if current_index == n:
        break

    # Calculate the cost to reverse all the strings up to the current index
    min_cost += sum(costs[:current_index])

# Step 5: Print the minimum cost
print(min_cost)
