def find_winner(M, X):
    winners = []
    for i in range(1, X+1):
        winner = (i - 1) % M + 1
        winners.append(winner)
    return winners

T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    winners = find_winner(M, X)
    print(*winners, sep=' ')
