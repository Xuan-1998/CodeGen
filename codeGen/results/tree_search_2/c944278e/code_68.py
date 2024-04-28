def winning_teams(s):
    n = len(s)
    return winning_teams_recursive(s, n)

# Example usage:
s = input()  # Read the binary string from standard input
n = int(input())  # Read the number of rounds from standard input
print(*winning_teams(s), sep='\n')  # Print all the winning teams
