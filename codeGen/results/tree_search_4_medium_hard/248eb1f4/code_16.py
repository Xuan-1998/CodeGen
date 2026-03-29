import sys
from functools import lru_cache

@lru_cache(None)
def find_winner(m, x):
    dp = [0]
    for i in range(1, x+1):
        if (i-1) % m == 0:
            dp.append((dp[-1]-1) % x + 1)
        else:
            dp.append(i % (x+1))
    return dp

T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    winners = find_winner(M, X)
    for winner in winners:
        print(winner, end=' ')
    print()
