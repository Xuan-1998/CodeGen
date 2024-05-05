def f(r):
    # calculate f(r) here
    return f(r)

t, l, r = map(int, input().split())
result = t0*f(l) + t1*f(l+1) + ... + tr - l*f(r)
print(result % (109 + 7))
