import sys
from math import comb

n = int(input())

table = [[0] * (2 ** n) for _ in range(n)]

for i in range(n):
    for j in range(2 ** n):
        if i == 0:
            table[i][j] = (j >> i) & 1
        else:
            max_score = 0
            for k in range(comb(2, i + 1)):
                bit_mask = ((k << i) | j) % (2 ** (i + 1))
                score = table[i - 1][bit_mask]
                if score > max_score:
                    max_score = score
            table[i][j] = max_score

winning_teams = [team for team in range(2 ** n) if table[-1][team]]

print(*sorted(winning_teams), sep='\n')
