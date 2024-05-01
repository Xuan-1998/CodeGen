from collections import defaultdict

def find_winning_teams(n):
    memo = defaultdict(list)
    skill_levels = [0] * (1 << n)

    def recursive_function(s, skill_levels, phase_numbers):
        if len(s) == 0:  # Base case: length of binary string becomes 0
            return [[], []]  # Return empty sets for winning teams

        next_phase_number = phase_numbers[0]
        next_skill_level = skill_levels[1 << n - 1]

        outcome_0 = recursive_function(s[:-1], [next_skill_level], phase_numbers[1:])
        outcome_1 = recursive_function(s[:-1], [skill_levels[1 << n - 2]], phase_numbers[1:])

        for winning_teams in memo[s]:
            if len(winning_teams) > 0 and skill_levels[next_phase_number] >= next_skill_level:
                # Update the sets of winning teams
                new_winning_teams = []
                for team in winning_teams:
                    if skill_levels[team + next_phase_number] >= next_skill_level:
                        new_winning_teams.append(team)
                memo[s].append(new_winning_teams)

        if s[-1] == '0':  # Update the sets of winning teams for outcome 0
            for winning_teams in memo[s[:-1]]:
                if len(winning_teams) > 0 and skill_levels[next_phase_number] >= next_skill_level:
                    new_winning_teams = []
                    for team in winning_teams:
                        if skill_levels[team + next_phase_number] >= next_skill_level:
                            new_winning_teams.append(team)
                    memo[s].append(new_winning_teams)

        return memo[s]

    # Call the recursive function with initial inputs
    result = find_winning_teams(n)
    print(result)
