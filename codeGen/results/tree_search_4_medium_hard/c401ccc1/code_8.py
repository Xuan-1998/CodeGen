def memoize(func):
    cache = {}
    def wrapper(i):
        if i not in cache:
            cache[i] = func(i)
        return cache[i]
    return wrapper

@memoize
def dp(i, memo={}):
    if i == 0:
        return True
    if i % 2 == 0:
        return dp(i // 2)
    else:
        return not dp((i - 1) & i)

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    if dp(v):
        print("YES")
    else:
        print("NO")
