import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
teams = [i for i in range(2**n)]
winners = []

def check_win(team):
    team_bin = bin(team)[2:].zfill(n)
    for i in range(n):
        if s[i] == '1' and int(team_bin[i]):
            return False
        elif s[i] == '0' and not int(team_bin[i]):
            return False
    return True

for team in teams:
    if check_win(team):
        winners.append(team)

winners.sort()
print('\n'.join(map(str, winners)))
