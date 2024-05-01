import sys
from functools import lru_cache

@lru_cache(maxsize=2**18)
def get_winners(n, s):
    if n == 0:
        return [s]

    winners = []
    for i in range(2**n):
        opponents = s[:i] + s[i+1:]
        if all(int(c) > int(opponents[j]) for j, c in enumerate(s[i])):
            winners += get_winners(n-1, opponents)
    return [s[i:] + s[:i] for i in range(2**n) if s[i:] in winners]

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    winners = list(set(get_winners(n, s)))
    winners.sort(key=lambda x: sum(int(c) for c in x))
    print('\n'.join(winners))

if __name__ == "__main__":
    main()
