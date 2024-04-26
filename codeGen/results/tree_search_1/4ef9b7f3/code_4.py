from collections import deque

def read_integers():
    return list(map(int, input().split()))

# Read the input
n = int(input())
initial_queue = read_integers()
k = int(input())
final_queue = read_integers()

# Use a deque for efficient popping from both ends
initial_queue = deque(initial_queue)
actions = []

# Try to match each monster in the final queue
for final_weight in final_queue:
    current_sum = 0
    while initial_queue and current_sum < final_weight:
        current_sum += initial_queue[0]
        if current_sum > final_weight:
            print("NO")
            exit()
        elif current_sum == final_weight:
            while current_sum > 0:
                if initial_queue and current_sum >= initial_queue[0]:  # Eat from the left
                    current_sum -= initial_queue[0]
                    actions.append(f"{len(initial_queue)} L")
                    initial_queue.popleft()
                elif initial_queue and current_sum >= initial_queue[-1]:  # Eat from the right
                    current_sum -= initial_queue[-1]
                    actions.append(f"{1} R")
                    initial_queue.pop()
        else:
            initial_queue.popleft()  # Continue summing up

# If we have matched all monsters in the final queue, output the actions
if not initial_queue:
    print("YES")
    for action in actions:
        print(action)
else:
    print("NO")
