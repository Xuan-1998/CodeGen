from collections import defaultdict

def coin_game(M, X):
    dp = defaultdict(dict)

    for i in range(1, X+1):
        winner = 0
        for j in range(i):
            if (M-1) % i < (M-2) % i or ((M-2) % i == 0 and j != 0):
                winner = (j+1)%i
            else:
                dp[i][winner] = j
                winner = (j+1)%i

        print(winner, end=' ')

    return


# Read input from standard input
T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    coin_game(M, X)
