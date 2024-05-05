def f(n):
    beauty_scores = [int(input()) for _ in range(n)]
    beauty_scores.sort(reverse=True)
    return n - 1

t, l, r = map(int, input().split())
result = t0 * f(l) + t1 * f(l + 1) + ... + tr - l * f(r)

print(result % (109 + 7))
