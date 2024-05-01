from collections import defaultdict

def tournament_winner(n, s):
    # Create a dictionary to store the skill levels of each team
    teams = defaultdict(int)

    # Initialize the cumulative skill level for each team
    cum_skills = [0] * (1 << n)

    # Iterate over the binary string to identify winning teams
    for i in range(n):
        for j in range(1 << n):  # loop through all possible combinations of teams
            if ((j >> i) & 1):  # check if team j is participating in this round
                cum_skills[j] += int(s[i])  # update the cumulative skill level

    winning_teams = []
    for j in range(1 << n):
        if cum_skills[j] == max(cum_skills):  # find teams with the highest cumulative skill level
            winning_teams.append(bin(j)[2:].zfill(n))  # convert team index to binary string and pad with zeros

    return sorted(winning_teams)

n = int(input())
s = input()
print(*tournament_winner(n, s), sep='\n')
