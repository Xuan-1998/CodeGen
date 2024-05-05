import sys

def find_winner(M, X):
    winners = []
    for i in range(1, X + 1):
        people = list(range(i))
        winner_idx = 0
        for _ in range(M - 1):
            winner_idx = (winner_idx + 1) % i
        winners.append(winner_idx)
    return winners

T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    winners = find_winner(M, X)
    print(*winners, sep='\n')
