def f(n):
    low = 1
    high = n

    while True:
        mid = (low + high) // 2

        if high - low == 1:
            return low

        if mid * (mid + 1) // 2 <= n:
            low = mid + 1
        else:
            high = mid

def solve(t, l, r):
    res = 0
    for i in range(l, r+1):
        res += t * f(i)
    return res % (10**9 + 7)

t, l, r = map(int, input().split())
print(solve(t, l, r))
