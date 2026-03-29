import sys

T = int(sys.stdin.readline())

for _ in range(T):
    M, X = map(int, sys.stdin.readline().split())
    winner_indices = []
    
    for i in range(X):
        if i % (M-1) == 0:  # after every (M-1) iterations
            winner_indices.append(i + 1)
    
    print(*winner_indices, sep='\n')
