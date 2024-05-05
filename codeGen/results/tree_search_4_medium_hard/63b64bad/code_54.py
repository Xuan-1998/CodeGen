from functools import lru_cache

@lru_cache(None)
def simulate(x, y):
    if x <= 0 or x > n:
        return -1
    
    next_x = max(2, (x + a[x] - 1) % n + 1)
    next_y = min(n, (y + a[x]) % n)
    
    if next_x == 1:
        return y
    else:
        return simulate(next_x, next_y)

n = int(input())
a = list(map(int, input().split()))
for i in range(2, n):
    print(simulate(i, 0))
