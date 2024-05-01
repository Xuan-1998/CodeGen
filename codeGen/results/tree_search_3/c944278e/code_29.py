import sys

def calculate_skill_levels(string):
    # Calculate skill levels based on winning/losing streaks
    skill_levels = [0] * (1 << n)
    for i in range(len(string)):
        team_id = int(string[i], 2)
        if string[i] == '1':
            skill_levels[team_id] += 1
        else:
            skill_levels[team_id] -= 1
    return skill_levels

def is_winnable(skill_levels):
    # Check if calculated skill levels satisfy the condition for a team to win the tournament
    for level in skill_levels:
        if level < 0 or level > 0:  # Only one team can have a negative skill level
            return False
    return True

n = int(sys.stdin.readline())
winning_teams = set()
for string in itertools.product('01', repeat=n):
    skill_levels = calculate_skill_levels(string)
    if is_winnable(skill_levels):
        winning_teams.add(tuple(sorted(map(int, string))))

print(*winning_teams, sep='\n')
