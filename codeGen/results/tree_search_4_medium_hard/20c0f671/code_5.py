from functools import lru_cache

@lru_cache(None)
def dp(i, w):
    if i == 0:
        return 0
    min_height = float('inf')
    for j in range(i):
        thickness = books[j][0]
        height = books[j][1]
        if w >= thickness:
            new_w = w - thickness
            min_height = min(min_height, dp(j, new_w) + height)
    return min_height

n, w = map(int, input().split())
books = []
for _ in range(n):
    t, h = map(int, input().split())
    books.append((t, h))

print(dp(n, w))
