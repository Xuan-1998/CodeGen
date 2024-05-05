import sys

def read_input():
    T = int(sys.stdin.readline().strip())
    return [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

def solve(M, X):
    winners = []
    for i in range(1, X+1):
        players = list(range(i))
        remaining_players = players[:]
        while len(remaining_players) > 1:
            player_index = (M-2) % len(remaining_players)
            del remaining_players[player_index]
        winners.append(remaining_players[0] if remaining_players else 0)
    return winners

def main():
    T = read_input()
    for M, X in T:
        print(*solve(M, X), sep='\n')

if __name__ == "__main__":
    main()
