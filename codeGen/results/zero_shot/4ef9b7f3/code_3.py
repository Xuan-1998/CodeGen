def simulate_eating(initial_queue, final_queue):
    i, j = 0, 0
    actions = []
    while i < len(final_queue):
        current_sum = 0
        start = j
        # Find a subsequence in the initial queue that matches the weight of the current monster in the final queue
        while j < len(initial_queue) and current_sum < final_queue[i]:
            current_sum += initial_queue[j]
            j += 1
        # If the weights do not match, it's impossible to form the final queue
        if current_sum != final_queue[i]:
            return "NO", []
        # Simulate the eating process
        while j - start > 1:
            if initial_queue[start] < initial_queue[j - 1]:
                actions.append(f"{start + 1} R")
                initial_queue[start] += initial_queue[j - 1]
                j -= 1
            else:
                actions.append(f"{start + 1} L")
                initial_queue[start + 1] += initial_queue[start]
                start += 1
        i += 1
    return "YES", actions

# Read input
n = int(input().strip())
initial_queue = list(map(int, input().strip().split()))
k = int(input().strip())
final_queue = list(map(int, input().strip().split()))

# Check for immediate impossibilities
if sum(initial_queue) != sum(final_queue):
    print("NO")
else:
    result, actions = simulate_eating(initial_queue, final_queue)
    print(result)
    if result == "YES":
        for action in actions:
            print(action)
