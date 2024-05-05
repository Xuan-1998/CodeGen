code
n = int(input())
m = int(input())
h = int(input())
s = list(map(int, input().split()))
total_players = sum(s)

if total_players < n:
    print(-1)
else:
    import math

    probability = 1 - math.comb(total_players - s[h-1], n-1) / math.comb(total_players, n)
    print(probability)
