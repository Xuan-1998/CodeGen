import sys
from collections import defaultdict

def calculate_probability():
    n, m, h = map(int, input().split())
    department_players = [int(x) for x in input().split()]
    
    # Count the number of players from each department who are not from the department of interest
    total_players = sum(department_players)
    not_from_department_h = total_players - department_players[h-1]
    
    if n > total_players:
        print(-1.0, file=sys.stdout)
        return
    
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    probability = 1.0
    for i in range(m):
        if i == h-1: continue
        players_from_department_i = department_players[i]
        probability *= (players_from_department_i + 1) / (total_players + 1)
    
    print(probability, file=sys.stdout)

if __name__ == "__main__":
    calculate_probability()
