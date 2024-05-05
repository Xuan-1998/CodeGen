import sys

def find_winner(M, X):
    winners = []
    for i in range(1, X+1):
        winner_index = (i - 1) % M + 1
        winners.append(winner_index)
    return winners

T = int(sys.stdin.readline())
for _ in range(T):
    M, X = map(int, sys.stdin.readline().split())
    winners = find_winner(M, X)
    print(*winners, sep=' ')
