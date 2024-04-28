import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
teams = [i for i in range(2**n)]
winners = []
for i in range(n):
    phase_teams = teams[:]
    if s[i] == '0':
        winners += teams[:2**(n-1-i)]
        teams = teams[2**(n-1-i):]
    else:
        winners += teams[-2**(n-1-i):]
        teams = teams[:-2**(n-1-i)]
winners.sort()
print('\n'.join(map(str, winners)))
