import sys
def find_winner(M, X):
    winners = []
    for i in range(1, X+1):
        winner_index = (i - 2) % i
        if M > 0:
            winner_index = (winner_index + M-1) % i
        winners.append(winner_index)
    return winners

T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    print(*find_winner(M, X), sep='\n')
