def winning_teams(n, s):
    # Initialize memoization dictionary
    memo = {(0,): [True]}

    for i in range(1 << n):
        # Calculate skill levels based on tournament results
        skill_levels = [(i >> j) & 1 for j in range(n)]
        state = tuple(skill_levels)

        if state not in memo:
            # Recursively update states and calculate new winning teams
            winning_teams = []
            for prev_state, prev_skill_levels in list(memo.items()):
                new_state = state[:prev_state.index(True)] + [True] + state[prev_state.index(True) + 1:]
                new_skill_levels = list(prev_skill_levels)
                new_skill_levels.append(sum(new_state))

                # Update memoization dictionary
                memo[new_state] = winning_teams + [(i >> j) & 1 for j in range(n)]

    # Find all winning teams and return them in ascending order
    winning_teams = [team for team, _ in sorted(memo.items()) if len(team) == n]

    return winning_teams

# Read input from stdin
n = int(input())
s = input()

# Print the winning teams to stdout
print(winning_teams(n, s))
