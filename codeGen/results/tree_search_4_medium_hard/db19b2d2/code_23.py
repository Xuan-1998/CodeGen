import sys

def solution():
    n, m, h = map(int, input().split())  # read inputs
    s = list(map(int, input().split()))  # read inputs
    total_players = sum(s)
    players_from_interest = s[h-1]
    team_formed = min(n, total_players) - (min(n, total_players) // m * (m - 1))
    
    if team_formed < 0:
        print(-1)
    else:
        probability = team_formed / n
        print(probability)

if __name__ == "__main__":
    solution()
