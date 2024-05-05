import sys

def winner_game(M, X):
    # Initialize the circle with indices from 1 to X
    circle = list(range(1, X+1))
    
    for _ in range(M-1):  # Pass the coin M-1 times
        prev_circle = circle.copy()
        circle = [(prev_circle[i-1] + i) % len(circle) for i in range(len(circle))]
    
    return circle[0]

T = int(sys.stdin.readline())
for _ in range(T):
    M, X = map(int, sys.stdin.readline().split())
    print(winner_game(M, X))
