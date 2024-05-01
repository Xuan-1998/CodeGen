from itertools import combinations

def tournament_winner(n):
    memo = {}
    winning_teams = set()

    def dp(phase, skills):
        if (phase, tuple(sorted(skills))) in memo:
            return memo[(phase, tuple(sorted(skills)))]

        winners = []
        for team_combination in combinations(range(2**n), len(skills)):
            skill_levels = [s[team-1] for team in team_combination]
            if all(skill_levels[i] >= skill_levels[j] for i in range(len(skill_levels)) for j in range(i+1, len(skill_levels))):
                winners.append(team_combination)

        memo[(phase, tuple(sorted(skills)))] = winners
        return winners

    for phase in range(n):
        skills = []
        for team in range(2**n):
            if (team >> phase) & 1:
                skills.append(int(input()))
            else:
                skills.append(-float('inf'))
        winners = dp(phase, skills)
        winning_teams.update(winners)

    return sorted(list(winning_teams))

if __name__ == "__main__":
    n = int(input())
    print(tournament_winner(n))
