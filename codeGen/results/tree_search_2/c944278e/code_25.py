from math import factorial
from itertools import permutations

def is_winning_team(teams, s):
    if not s:  # base case: empty string
        return True

    result = 0
    for i in range(len(s)):
        if s[i] == '1':
            result ^= 1 << (n - i - 1)
    winning_teams = []
    for p in permutations(teams):
        if is_winning_team(list(p), s[1:]):
            winning_teams.append(''.join(map(str, p)))
    return winning_teams

n = int(input())
s = input()
print(*is_winning_team([i for i in range(2**n)], s), sep='\n')
