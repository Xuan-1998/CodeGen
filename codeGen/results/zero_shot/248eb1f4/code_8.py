import sys

def process_input():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        M, X = map(int, sys.stdin.readline().strip().split())
        yield M, X

for M, X in process_input():
    winners = [0] * (X + 1)
    for i in range(2, X + 1):
        winners[i] = (winners[i - 1] + M) % i
    print(*winners[1:], sep='\n')
