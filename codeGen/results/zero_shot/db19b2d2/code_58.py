import sys

def calculate_probability():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    # Calculate the total number of players
    total_players = sum(s)
    
    # If there are not enough basketball players in the university to form a team, output -1 instead.
    if total_players < n:
        print(-1)
    else:
        # Calculate the probability that a randomly formed team will have at least one player from the department of interest
        probability = 1 - sum((n - i) * (s[h] < i) for i in range(1, n + 1)) / total_players
        
        print(probability)

if __name__ == "__main__":
    calculate_probability()
