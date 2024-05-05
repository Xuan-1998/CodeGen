n, m, h = map(int, input().split())
s = list(map(int, input().split()))

total_players = sum(s)

players_from_h = s[h-1]

probability = min(1, (players_from_h + 1) / (total_players + 1))

if total_players < n:
    print(-1)
else:
    print(probability)
