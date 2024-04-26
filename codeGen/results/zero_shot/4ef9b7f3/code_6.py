def find_eating_order(n, initial, k, final):
    # Check for immediate impossibility
    if sum(initial) != sum(final):
        return "NO"

    # Indices for initial and final queues
    i, j = 0, 0
    # Stores the order of eating
    eating_order = []
    while j < k:
        # Current weight to match in the final queue
        current_weight = final[j]
        temp_weight = 0
        # Find monsters in the initial queue that can combine to the current weight
        while i < n and temp_weight < current_weight:
            temp_weight += initial[i]
            i += 1
        if temp_weight != current_weight:
            return "NO"
        # If we found a match, we backtrack to find the eating order
        for eat in range(i - 1, i - (i - j) - 1, -1):
            if eat == i - 1:
                eating_order.append(f"{eat - j + 1} R")
            else:
                eating_order.append(f"{eat - j + 1} L")
        j += 1

    return "\n".join(["YES"] + eating_order)

# Read input from stdin
n = int(input().strip())
initial = list(map(int, input().strip().split()))
k = int(input().strip())
final = list(map(int, input().strip().split()))

# Get the eating order or determine it's impossible
result = find_eating_order(n, initial, k, final)
print(result)
