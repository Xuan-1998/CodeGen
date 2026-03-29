import sys
from collections import deque

# Read input from standard input
board = list(input())
hand = list(input())

# Create a queue for BFS, with the initial state being the board
queue = deque([(board, 0)])  # (board state, number of moves)

while queue:
    state, moves = queue.popleft()
    
    if len(state) == 0:  # If all balls have been removed, return the number of moves
        print(moves)
        sys.exit(0)
        
    for i in range(len(state)):
        if len(set(state[i])) == 1 and len(state) - (i + 1) >= 3:
            state = state[:i] + [''] * 3 + state[i + 3:]
            queue.append((state, moves + 1))
            
    for i in range(len(state)):
        if set([state[i]]).issubset(set(['R', 'Y', 'B', 'G', 'W'])):
            state = state[:i] + [''] * (4 - len(set([state[i]]))) + state[i + 1:]
            queue.append((state, moves + 1))

print(-1)  # If it is not possible to remove all the balls
