from sys import stdin

def find_sequence(initial_queue, target_weight):
    current_weight = 0
    sequence = []
    while initial_queue and current_weight < target_weight:
        sequence.append(initial_queue.pop(0))
        current_weight += sequence[-1]
    return sequence if current_weight == target_weight else None

def record_eating_sequence(sequence):
    actions = []
    while len(sequence) > 1:
        if sequence[0] < sequence[-1]:
            actions.append(f"1 L")
            sequence[1] += sequence[0]
            sequence.pop(0)
        else:
            actions.append(f"{len(sequence)} R")
            sequence[-2] += sequence[-1]
            sequence.pop()
    return actions

# Read input
n = int(stdin.readline().strip())
initial_queue = list(map(int, stdin.readline().strip().split()))
k = int(stdin.readline().strip())
final_queue = list(map(int, stdin.readline().strip().split()))

# Process the queues
actions = []
possible = True
for target in final_queue:
    sequence = find_sequence(initial_queue, target)
    if sequence is None:
        possible = False
        break
    actions.extend(record_eating_sequence(sequence))

# Output the result
if possible:
    print("YES")
    for action in actions:
        print(action)
else:
    print("NO")
