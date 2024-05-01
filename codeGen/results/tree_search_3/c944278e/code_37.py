import sys

def get_winners(skill_level, phase_result):
    # Initialize memoization cache and winning teams set
    memo = {}
    winning_teams = set()

    def recursive_get_winners(skill_level, phase_result):
        nonlocal memo, winning_teams

        # Check if we've already calculated this state
        if (skill_level, phase_result) in memo:
            return memo[(skill_level, phase_result)]

        # Calculate the winners for this state
        winners = set()
        for i in range(2**len(bin(phase_result))):
            team_skill = int(format(i, 'b').zfill(len(str(skill_level))), 2)
            if (team_skill <= skill_level and phase_result & (1 << len(bin(team_skill))-1-i)) or \
               (team_skill > skill_level):
                winners.add(team_skill)

        # Memoize the result
        memo[(skill_level, phase_result)] = winners

        return winners

    recursive_get_winners(skill_level, int(phase_result, 2))

    return sorted(winning_teams)

# Read input from stdin
n = int(sys.stdin.readline())
phase_results = [int(x, 2) for x in sys.stdin.read().split()]

# Calculate and print the winning teams
winning_teams = get_winners(0, 0)
for i, phase_result in enumerate(phase_results):
    winning_teams.update(recursive_get_winners(i+1, phase_result))

print('\n'.join(map(str, sorted(winning_teams))))
