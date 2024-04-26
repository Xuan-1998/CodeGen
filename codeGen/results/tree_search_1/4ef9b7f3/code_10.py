from sys import stdin

# Read input from stdin
n = int(stdin.readline().strip())
initial_queue = list(map(int, stdin.readline().strip().split()))
k = int(stdin.readline().strip())
final_queue = list(map(int, stdin.readline().strip().split()))

# Initialize pointers and variables
left = 0
right = 0
current_weight = initial_queue[0]
operations = []

# Function to perform the operations
def merge_monsters():
    global left, right, current_weight
    for weight in final_queue:
        # Check if the current weight matches the target weight
        if current_weight == weight:
            continue
        # Expand the segment to match the target weight
        while right < n - 1 and current_weight < weight:
            right += 1
            current_weight += initial_queue[right]
            operations.append((left + 1, 'R'))
        while left < right and current_weight < weight:
            left += 1
            current_weight += initial_queue[left]
            operations.append((left, 'L'))
        # Check if we matched the target weight
        if current_weight != weight:
            return False
        # Reset pointers for the next target weight
        if right < n - 1:
            right += 1
            current_weight = initial_queue[right]
            left = right
        elif left > 0:
            left -= 1
            current_weight = initial_queue[left]
            right = left
        else:
            return False
    return True

# Perform the merging operations
if merge_monsters() and current_weight == final_queue[-1]:
    print("YES")
    for op in operations:
        print(*op)
else:
    print("NO")
