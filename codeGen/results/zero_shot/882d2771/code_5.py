import sys

t, l, r = map(int, input().split())

def f(n):
    # calculate the minimal total number of pairwise comparisons needed
    return n - 1

result = sum(t*(l+i-1) for i in range(1, r-l+2)) - (l*r-l)

print(result % (10**9 + 7))
