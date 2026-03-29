import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def can_reach(i, k):
    if i == 0:
        return True
    for j in range(1, min(i, k) + 1):
        if can_reach(j - 1, k) and (i - j) % (k-1) in [0, 1]:
            return True
    return False

def main():
    n = int(input())
    stones = list(map(int, input().split()))
    k = (stones[-1] - stones[0]) // len(stones)
    dp_stone = {}
    for i in range(n):
        if i > 0:
            for j in range(1, min(i, k) + 1):
                if can_reach(j-1, k) and (i-j) % (k-1) in [0, 1]:
                    dp_stone[i] = True
                    break
        else:
            dp_stone[0] = True
    print('YES' if dp_stone[n-1] else 'NO')

if __name__ == '__main__':
    main()
