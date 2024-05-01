def findWinningTeams(n, s):
    # Check if input data is valid
    if len(s) != 2**n:
        return "Invalid input"

    # Initialize a dictionary to store the winning teams and their points
    winning_teams = {}

    # Iterate through each phase of the tournament
    for i in range(len(s)):
        # Generate all possible combinations of teams that could win in this phase
        for j in range(2**i):
            team_id = format(j, 'b').zfill(i+1)
            # Evaluate if this team wins in this phase
            if s[i] == '1' and all(int(x) for x in team_id):
                # Add this team to the winning teams dictionary with its points
                if team_id not in winning_teams:
                    winning_teams[team_id] = 0
                winning_teams[team_id] += 1

    # Sort the winning teams by their points and return them
    sorted_teams = sorted(winning_teams.items(), key=lambda x: x[1], reverse=True)
    return [team for team, _ in sorted_teams]

# Example usage:
n = int(input())
s = input()
print(findWinningTeams(n, s))
