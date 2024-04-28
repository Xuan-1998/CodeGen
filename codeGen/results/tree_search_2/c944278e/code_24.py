import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

winning_teams = set()
current_skill_level = 0

for i in range(n):
    if s[i] == '0':
        current_skill_level += 2 ** (n - i - 1)
    else:
        current_skill_level -= 2 ** (n - i - 1)

winning_teams.add(current_skill_level)

print(' '.join(map(str, sorted(list(winning_teams)))))
