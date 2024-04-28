import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
teams = [i for i in range(2**n)]
for i in range(n):
    teams = [team for team in teams if ((team >> i) & 1) == (int(s[i]))]
print(*sorted([bin(team).count('1') for team in teams]), sep='\n')
