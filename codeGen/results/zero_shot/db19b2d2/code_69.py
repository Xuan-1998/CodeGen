import sys

def calculate_probability():
    # Read input from stdin
    n, m, h = map(int, sys.stdin.readline().split())
    department_sizes = list(map(int, sys.stdin.readline().split()))

    # Calculate the total number of basketball players
    total_players = sum(department_sizes)

    # Check if there are not enough basketball players to form a team
    if total_players < n:
        print(-1)
        return

    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    p = department_sizes[h - 1] / total_players
    q = 1 - p
    probability = 1 - (q ** n)

    # Print the answer to stdout with 6 decimal places
    print(f"{probability:.6f}")

calculate_probability()
