python
def find_winner(M, X):
    winners = [i + 1 for i in range(X)]
    return winners[:X]
