from math import floor
from functools import lru_cache

@lru_cache(maxsize=None)
def min_squares(n, m):
    if n == 0 or m == 0:
        return 0
    
    min_count = float('inf')
    
    for k in range(1, min(n, m) + 1):
        if n >= k and m >= k:
            count = min_squares(floor((n - k) / k), floor((m - k) / k)) + 1
            min_count = min(min_count, count)
    
    return min_count

def main():
    n, m = map(int, input().split())
    print(min_squares(n, m))

if __name__ == "__main__":
    main()
