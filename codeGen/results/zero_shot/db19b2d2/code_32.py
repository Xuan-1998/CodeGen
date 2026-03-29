import math

def get_total_players(m, s):
    return sum(s)

def get_probability(n, total_players, players_from_interest):
    numerator = math.comb(players_from_interest, 1)
    denominator = math.comb(total_players, n)
    return numerator / denominator

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

total_players = get_total_players(m, s)

if total_players < n:
    print(-1)
else:
    players_from_interest = s[h-1]
    probability = get_probability(n, total_players, players_from_interest)
    print(probability)
