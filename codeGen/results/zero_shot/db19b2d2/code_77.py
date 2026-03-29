import math

n, m, h = map(int, input().split())
si = list(map(int, input().split()))

n_total_players = sum(si for si in range(1, m+1))

if n_total_players < n:
    print(-1)
else:
    p = si[h-1]
    num_ways_to_choose_players = 1
    for i in range(n):
        num_ways_to_choose_players *= (m - h + 1 if i < p else m)
    prob = num_ways_to_choose_players / math.comb(n_total_players, n)
    print(prob)
