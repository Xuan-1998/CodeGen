def find_eating_order(n, initial_queue, k, final_queue):
    # Step 1: Check if the sum of the weights is equal
    if sum(initial_queue) != sum(final_queue):
        return "NO"
    
    # Step 2: Check if each final weight can be formed from the initial queue
    final_index = 0
    initial_start = 0
    initial_end = 0
    eating_order = []

    while final_index < k and initial_start < n:
        current_sum = 0
        while initial_end < n and current_sum < final_queue[final_index]:
            current_sum += initial_queue[initial_end]
            initial_end += 1

        if current_sum != final_queue[final_index]:
            return "NO"

        # Step 3: Find the order of eating
        while initial_end - initial_start > 1:
            if initial_queue[initial_start] < initial_queue[initial_end - 1]:
                eating_order.append(f"{initial_end - initial_start} L")
                initial_queue[initial_start + 1] += initial_queue[initial_start]
                initial_start += 1
            else:
                eating_order.append(f"{initial_end - initial_start} R")
                initial_queue[initial_end - 2] += initial_queue[initial_end - 1]
                initial_end -= 1

        final_index += 1
        initial_start = initial_end

    if final_index == k:
        return "YES\n" + "\n".join(eating_order)
    else:
        return "NO"

# Read input from stdin
n = int(input())
initial_queue = list(map(int, input().split()))
k = int(input())
final_queue = list(map(int, input().split()))

# Get the eating order or determine if it's impossible
result = find_eating_order(n, initial_queue, k, final_queue)

# Print the result to stdout
print(result)
