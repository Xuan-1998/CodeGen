from sys import stdin
mem = {}

def dp(d, f):
    if d <= 0 or (d, f) in mem:
        return max(0, d * min(f, abs(f - d)))
    for s in range(min(f, abs(f - d)) + 1):
        res = max(res if (d1, s) in mem else dp(d - 1, s), 0)
    return res

f, t = map(int, stdin.readline().split())
v, V = map(int, stdin.readline().split())

print(dp(t, min(V, abs(V - v))))
