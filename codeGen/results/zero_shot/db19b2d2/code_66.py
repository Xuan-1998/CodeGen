n = int(input())
m = int(input())
h = int(input())
s = list(map(int, input().split()))

total_players = sum(s)

min_required = s[h-1]

max_teams = total_players // min_required

from math import comb
prob = max_teams / comb(total_players, n)

if total_players < n:
    print(-1)
else:
    print(prob)
