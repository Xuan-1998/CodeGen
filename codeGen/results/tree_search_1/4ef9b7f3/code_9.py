from collections import deque

def find_subsequence(queue, target_weight):
    subseq_weight = 0
    actions = []
    while queue and subseq_weight != target_weight:
        if subseq_weight < target_weight:
            subseq_weight += queue[0]
            if len(actions) > 0 and actions[-1][1] == 'L':
                actions[-1] = (actions[-1][0], 'L')
            else:
                actions.append((1, 'L'))
            queue.popleft()
        elif subseq_weight > target_weight:
            return False, []
    return subseq_weight == target_weight, actions

def solve_monsters_eating(n, initial_queue, k, final_queue):
    queue = deque(initial_queue)
    all_actions = []

    for weight in final_queue:
        possible, actions = find_subsequence(queue, weight)
        if not possible:
            return "NO"
        all_actions.extend(actions)

    return all_actions

# Read input
n = int(input().strip())
initial_queue = list(map(int, input().strip().split()))
k = int(input().strip())
final_queue = list(map(int, input().strip().split()))

# Solve the problem
result = solve_monsters_eating(n, initial_queue, k, final_queue)

# Output the result
if result == "NO":
    print(result)
else:
    print("YES")
    for action in result:
        print(f"{action[0]} {action[1]}")
