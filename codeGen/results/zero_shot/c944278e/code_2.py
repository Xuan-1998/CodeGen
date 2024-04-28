import sys
from collections import defaultdict

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
skill_levels = [i for i in range(2**n)]

winning_teams = []

for i in range(len(s)):
    for j in range(i+1, len(s)):
        if (s[i] == '0' and s[j] == '1') or (s[i] == '1' and s[j] == '0'):
            skill_levels.remove(int('1' + s[:i] + '0' + s[i+1:j] + '1' + s[j+1:], 2))

for team in skill_levels:
    print(team)
