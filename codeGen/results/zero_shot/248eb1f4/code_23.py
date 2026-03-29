    import sys

    def calculate_winner(M, X):
        winners = []
        for i in range(1, X+1):
            remaining_players = list(range(1, i+1))
            current_winner_index = (i - 2) % len(remaining_players)
            winner_index = remaining_players[current_winner_index]
            winners.append(winner_index)
        return winners

    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        M, X = map(int, sys.stdin.readline().strip().split())
        winners = calculate_winner(M, X)
        print(*winners, sep='\n')
