min_cost = 0

for i in range(n):
    # Find the first string that is larger than the current one
    j = i + 1
    while j < n and strings[j] <= strings[i]:
        j += 1
    
    # Calculate the cost of reversing all strings between i and j-1
    min_cost += sum(costs[i:j])
    
    # Update i to be j
    i = j - 1

print(min_cost)
