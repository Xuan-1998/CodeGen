import sys
from math import comb

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    # Calculate total number of basketball players
    total_players = sum(s)
    
    # If there are not enough basketball players to form a team, output -1
    if total_players < n:
        print(-1.0)
        return
    
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob = 1.0
    for i in range(h):
        prob *= (s[i] / total_players) ** comb(n-1, i)
    
    print(prob)

if __name__ == "__main__":
    solve()
