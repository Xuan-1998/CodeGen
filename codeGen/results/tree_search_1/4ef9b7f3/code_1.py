from collections import deque

def find_subsequence(queue, target):
    subseq = deque()
    total = 0
    while queue and total < target:
        total += queue[0]
        subseq.append(queue.popleft())
    return subseq if total == target else None

def simulate_eating(subseq):
    moves = []
    while len(subseq) > 1:
        if subseq[0] >= subseq[-1]:
            moves.append((len(subseq), 'L'))
            subseq[0] += subseq[1]
            subseq.popleft()
        else:
            moves.append((1, 'R'))
            subseq[-1] += subseq[-2]
            subseq.pop()
    return moves

def solve_monsters(initial, final):
    moves = []
    initial_queue = deque(initial)
    
    for final_monster in reversed(final):
        subseq = find_subsequence(initial_queue, final_monster)
        if subseq is None:
            return "NO"
        moves.extend(simulate_eating(subseq))
    
    if initial_queue:
        return "NO"
    
    return ["YES"] + moves

# Read input
n = int(input().strip())
initial_monsters = list(map(int, input().strip().split()))
k = int(input().strip())
final_monsters = list(map(int, input().strip().split()))

# Solve the problem
result = solve_monsters(initial_monsters, final_monsters)

# Output the result
if result == "NO":
    print(result)
else:
    print(result[0])
    for move in result[1:]:
        print(f"{move[0]} {move[1]}")
