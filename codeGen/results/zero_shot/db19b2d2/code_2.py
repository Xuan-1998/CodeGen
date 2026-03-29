import math
n, m, h = map(int, input().split())
s = list(map(int, input().split()))
team_size = n // 5 + (1 if n % 5 > 0 else 0)
total_players = sum(s)
players_from_h = s[h-1]

if total_players < team_size:
    print(-1)
else:
    probability = 0
    for i in range(m):
        players_in_i = s[i]
        if i == h - 1:
            players_in_i += players_from_h
        probability += players_in_i / total_players
    probability *= (1 - math.pow(1 - team_size / total_players, team_size))
    print(probability)
