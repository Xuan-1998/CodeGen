import math

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

total_teams = math.comb(m, n)
teams_with_h_player = math.comb(m-1, n-1) * s[h-1]

probability = teams_with_h_player / total_teams

print(probability if probability <= 1 else -1)
