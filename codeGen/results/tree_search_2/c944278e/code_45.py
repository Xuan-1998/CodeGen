def win_team(teams, n):
    if len(teams) == 1:
        return [teams[0]]
    max_skill = 0
    winner = None
    for i in range(len(teams)):
        team = teams[i]
        skills = sum([int(input(f"Enter skill level of team {i+1}: ")) for j in range(n)])
        if skills > max_skill:
            max_skill = skills
            winner = team
    winners = win_team([team for i, team in enumerate(teams) if i != teams.index(winner)], n)
    return [winner] + winners

n = int(input("Enter the number of teams: "))
print(*win_team([(i+1) for i in range(2**n)], n), sep='\n')
