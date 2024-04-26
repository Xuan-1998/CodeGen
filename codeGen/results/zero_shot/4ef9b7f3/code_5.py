from collections import deque

def find_eating_order(n, initial, k, final):
    initial_queue = deque(initial)
    final_queue = deque(final)
    operations = []

    while final_queue:
        current_final = final_queue.popleft()
        current_sum = 0
        temp_operations = []

        # Try to match the current final monster's weight
        while initial_queue and current_sum < current_final:
            current_sum += initial_queue[0]
            temp_operations.append(('L', initial_queue.popleft()))

        if current_sum != current_final:
            # If we can't match it, the transformation is impossible
            return "NO"
        
        # Record the operations in reverse, as we have recorded them from left to right
        for i, (direction, _) in enumerate(reversed(temp_operations), 1):
            operations.append(f"{i} {direction}")

    return "YES\n" + "\n".join(operations)

# Read input
n = int(input().strip())
initial_monsters = list(map(int, input().strip().split()))
k = int(input().strip())
final_monsters = list(map(int, input().strip().split()))

# Find and print the eating order
result = find_eating_order(n, initial_monsters, k, final_monsters)
print(result)
