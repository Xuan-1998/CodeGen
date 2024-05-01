def find_winning_teams(score):
    if score == 1:
        return [[i] for i in range(2**n)]

    if score in memo:
        return memo[score]

    winning_teams = []
    for i in range(2**n):
        if (s[i-1] & 1) and (i >> (n-1)):
            new_score = calculate_new_score(i, s)
            teams = find_winning_teams(new_score)
            for team in teams:
                winning_teams.append([i] + team)

    memo[score] = winning_teams
    return winning_teams

def main():
    memo = {}
    winning_teams_per_phase = []
    for i in range(2**n):
        teams = find_winning_teams(i)
        winning_teams_per_phase.append([team for team in teams])

    all_winning_teams = [item for sublist in winning_teams_per_phase for item in sublist]
    return all_winning_teams

print(main())
