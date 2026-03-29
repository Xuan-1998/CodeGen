import sys

def calculate_max_profit():
    # Read input from standard input
    n, m, c0, d0 = map(int, sys.stdin.readline().split())
    stuffings = []
    
    for _ in range(m):
        ai, bi, ci, di = map(int, sys.stdin.readline().split())
        stuffings.append((ai, bi, ci, di))
    
    # Your solution goes here
    max_profit = 0
    
    return str(max_profit)

print(calculate_max_profit())
