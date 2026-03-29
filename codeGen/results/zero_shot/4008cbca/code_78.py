import sys
from collections import deque

def solve():
    board = input().strip()
    hand = input().strip()

    # Create a graph to represent the game state
    graph = {}
    for i, b in enumerate(board):
        if b not in graph:
            graph[b] = []
        if i > 0 and board[i-1] == b:
            continue
        if i < len(board) - 1 and board[i+1] == b:
            continue
        for h in hand:
            if h != b:
                graph[h].append(i)

    # Perform BFS to find the minimum number of balls to insert
    queue = deque([(0, [board])])
    visited = set()
    while queue:
        state, history = queue.popleft()
        if board not in history and all(h in history for h in hand):
            return len(history) - 1
        if state not in visited:
            visited.add(state)
            for i, b in enumerate(board):
                if i > 0 and b == board[i-1]:
                    continue
                if i < len(board) - 1 and b == board[i+1]:
                    continue
                for h in hand:
                    if h != b and state + (i,) not in visited:
                        queue.append((state + (i,), history + [b]))
    return -1

print(solve())
