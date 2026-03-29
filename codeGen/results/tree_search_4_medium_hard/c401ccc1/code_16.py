def f(u, v, memo):
    if (u & v) == v:
        return True

    dp = [[False] * (1 << 30) for _ in range((1 << 30))]
    for w in range(1 << 30):
        if (u & w) == w and f(w, v, memo):
            return True
    return False

memo = {}

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print("YES" if f(u, v, memo) else "NO")
