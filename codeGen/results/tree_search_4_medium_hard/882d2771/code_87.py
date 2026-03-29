=begin
def f(r, k):
    if r <= 1:
        return 0
    res = float('inf')
    for i in range(min(k + 1, r), -1, -1):
        res = min(res, f(r - 1, i - 1) + (k - i))
    return res

t, l, r = map(int, input().split())
res = 0
for i in range(t):
    res += i * f(min(l + i, r), min(i, t - 1 - i))
res -= l * f(r)
print(res % (10**9 + 7))
=end
