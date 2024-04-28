import sys
from functools import lru_cache

@lru_cache(None)
def find_winners(n, s):
    if n == 1:
        return [s]

    winners = []
    for i in range(2**n):
        winner = (i >> (n-1)) & 1
        if winner == 1:
            winners.extend(find_winners(n-1, bin(i)[2:]))
        else:
            winners.extend([s])
    
    return winners

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    winners = find_winners(n, s)
    for winner in sorted(winners):
        print(winner)

if __name__ == "__main__":
    main()
