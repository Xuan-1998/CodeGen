n = int(input())
s = input()

teams = [i for i in range(2**n)]
winning_teams = []

for i in range(n):
    s_phase = list(map(int, s[i*2:i*2+2]))
    teams = [team for team in teams if (s_phase[0] > s_phase[1]) == ((team >> i) & 1)]

print(*sorted(teams))
