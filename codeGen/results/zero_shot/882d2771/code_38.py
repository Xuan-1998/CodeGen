from math import gcd
def f(n):
    if n == 1:
        return 0
    else:
        return (n-1) + f(n-1)

t, l, r = map(int, input().split())
result = t * f(l)
for i in range(1, r-l+2):
    result += t * f(l+i)
result -= l * f(r)
print(result % (10**9 + 7))
