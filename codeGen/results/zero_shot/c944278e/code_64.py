import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
skill_levels = [i for i in range(2**n)]
winning_teams = set()

for bit in range(n):
    low = 0
    high = len(skill_levels) - 1
    while low <= high:
        mid = (low + high) // 2
        if s[bit] == '0':
            winning_teams.update(set(range(mid+1)))
            skill_levels = skill_levels[:mid]
        else:
            winning_teams.update(set(range(mid, len(skill_levels))))
            skill_levels = skill_levels[mid+1:]
    winning_teams = {i for i in winning_teams if (s[bit] == '0' and i < 2**n//2) or (s[bit] == '1' and i >= 2**n//2)}
print(*sorted(winning_teams))
