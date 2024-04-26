def simulate_eating(n, initial_queue, k, final_queue):
    initial_ptr = 0
    final_ptr = 0
    actions = []

    while final_ptr < k:
        current_weight = initial_queue[initial_ptr]
        action_list = []

        # Combine monsters until their weight matches the current monster in the final queue
        while current_weight < final_queue[final_ptr]:
            initial_ptr += 1
            if initial_ptr == n or current_weight + initial_queue[initial_ptr] > final_queue[final_ptr]:
                # If we can't match the weight or exceed it, it's impossible to form the final queue
                return "NO"
            current_weight += initial_queue[initial_ptr]
            action_list.append('R')

        if current_weight != final_queue[final_ptr]:
            # If the total weight doesn't match exactly, it's impossible to form the final queue
            return "NO"

        # Record the actions for this round
        monster_index = final_ptr + 1
        for action in reversed(action_list):
            actions.append(f"{monster_index} {action}")

        initial_ptr += 1
        final_ptr += 1

    return "YES\n" + "\n".join(actions)

# Read input
n = int(input().strip())
initial_queue = list(map(int, input().strip().split()))
k = int(input().strip())
final_queue = list(map(int, input().strip().split()))

# Validate total weight
if sum(initial_queue) != sum(final_queue):
    print("NO")
else:
    result = simulate_eating(n, initial_queue, k, final_queue)
    print(result)
