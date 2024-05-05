import sys

def f(n):
    # TO DO: implement dynamic programming here
    pass

t, l, r = map(int, input().split())
result = 0
for i in range(l, r + 1):
    result += t * f(i) - (l if i == l else 0)
print(result % (10**9 + 7))
