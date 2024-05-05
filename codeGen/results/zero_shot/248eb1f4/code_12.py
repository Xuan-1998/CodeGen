import sys

def find_winner(M, X):
    winners = []
    for i in range(1, X+1):
        winner_index = (i + M - 1) % i
        winners.append(winner_index)
    return winners

T = int(sys.stdin.readline())
for _ in range(T):
    M, X = map(int, sys.stdin.readline().split())
    print(*find_winner(M, X), sep='\n')
