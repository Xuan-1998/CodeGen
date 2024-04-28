import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

winning_teams = []

def calculate_skill(level):
    skill = 0
    for i in range(n-1, -1, -1):
        if s[i] == '1':
            skill += 2**i
    return level + skill

for i in range(2**n):
    if calculate_skill(i) == max([calculate_skill(j) for j in range(2**n)]):
        winning_teams.append(bin(i)[2:].zfill(n))

winning_teams.sort()
print('\n'.join(winning_teams))
