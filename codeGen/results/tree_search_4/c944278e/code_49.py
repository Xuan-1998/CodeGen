import sys

def solve():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()

    # Initialize an empty set to store the winning teams
    winning_teams = set()

    for i in range(n):
        if s[i] == '1':
            # Update the winning teams for this phase
            winning_teams.update(2**i - 1)

    print(*winning_teams, sep='\n')

if __name__ == "__main__":
    solve()
