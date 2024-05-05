t, l, r = map(int, input().split())

def f(n):
    return n-1

t0 = (l - 1)
t1 = (l+1 - 1)
tn = (r - 1)

print(((t0*f(l)) + (t1*f(l+1))) + ... + ((tn*f(r)) - l*f(r)))
