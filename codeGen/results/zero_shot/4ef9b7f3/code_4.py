def find_eating_order(n, initial_queue, k, final_queue):
    # Check if the sum of both queues is equal
    if sum(initial_queue) != sum(final_queue):
        return "NO"

    # Initialize variables
    result = []
    start = 0  # Start pointer for the initial queue
    end = n - 1  # End pointer for the initial queue

    # Iterate through each monster in the final queue
    for final_monster in final_queue:
        current_weight = 0
        operations = []

        # Try to match the final monster from the start
        while start <= end and current_weight < final_monster:
            current_weight += initial_queue[start]
            operations.append((start + 1, 'L'))
            start += 1

        # If not matched, reset and try from the end
        if current_weight != final_monster:
            current_weight = 0
            operations = []
            while start <= end and current_weight < final_monster:
                current_weight += initial_queue[end]
                operations.append((end - start + 1, 'R'))
                end -= 1

        # If still not matched, it's impossible
        if current_weight != final_monster:
            return "NO"

        # Add the operations for this monster to the result
        result.extend(operations[:-1])  # Exclude the last operation

    # If we reach here, it's possible
    return ["YES"] + result

# Read input from stdin
n = int(input().strip())
initial_queue = list(map(int, input().strip().split()))
k = int(input().strip())
final_queue = list(map(int, input().strip().split()))

# Find the eating order and print the result
result = find_eating_order(n, initial_queue, k, final_queue)
print('\n'.join(map(str, result)) if result[0] == "YES" else "NO")
