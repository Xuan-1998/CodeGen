def find_winner(M, X):
    winners = []
    for i in range(1, X+1):
        winner_index = (i-1) + ((M-1) % (i-1))
        winners.append(winner_index)
    return winners

T = int(input())  # number of test cases
for _ in range(T):
    M, X = map(int, input().split())
    print(' '.join(map(str, find_winner(M, X))))
