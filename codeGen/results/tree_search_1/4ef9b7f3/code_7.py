def find_eating_order(n, initial_queue, k, final_queue):
    actions = []
    start = 0
    for b in final_queue:
        sum_weights = 0
        count = 0
        while start < n and sum_weights < b:
            sum_weights += initial_queue[start]
            start += 1
            count += 1
        if sum_weights != b:
            return "NO", []
        # Record the sequence of actions
        for i in range(count - 1):
            if i == 0:
                actions.append(f"{1} R")
            else:
                actions.append(f"{1} L")
    return "YES", actions

# Read input from stdin
n = int(input().strip())
initial_queue = list(map(int, input().strip().split()))
k = int(input().strip())
final_queue = list(map(int, input().strip().split()))

# Find the eating order
result, eating_order = find_eating_order(n, initial_queue, k, final_queue)

# Print the result to stdout
print(result)
if result == "YES":
    for action in eating_order:
        print(action)
