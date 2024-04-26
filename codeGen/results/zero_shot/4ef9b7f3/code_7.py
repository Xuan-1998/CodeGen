from collections import deque

# Read input
n = int(input())
initial_queue = list(map(int, input().split()))
k = int(input())
final_queue = list(map(int, input().split()))

# Step 1: Verify the possibility
def is_possible(initial_queue, final_queue):
    i, j = 0, 0
    while i < n and j < k:
        sum_weights = initial_queue[i]
        i += 1
        while i < n and sum_weights < final_queue[j]:
            sum_weights += initial_queue[i]
            i += 1
        if sum_weights != final_queue[j]:
            return False
        j += 1
    return j == k

# Step 2: Find the sequence of actions
def find_sequence(initial_queue, final_queue):
    actions = []
    i, j = 0, 0
    initial_deque = deque(initial_queue)
    while j < k:
        sum_weights = initial_deque[0]
        sequence = []
        while sum_weights < final_queue[j]:
            if initial_deque[-1] > initial_deque[0]:
                sum_weights += initial_deque.pop()
                sequence.append('R')
            else:
                sum_weights += initial_deque.popleft()
                sequence.append('L')
        actions.append(sequence)
        j += 1
    return actions

# Main logic
if is_possible(initial_queue, final_queue):
    print("YES")
    actions = find_sequence(initial_queue, final_queue)
    idx = 1
    for sequence in actions:
        for action in sequence:
            print(idx, action)
        idx += 1
else:
    print("NO")
