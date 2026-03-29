import sys

t, l, r = map(int, input().split())
# Define the function f(n)
def f(n):
    # TO DO: implement the recursive formula for f(n)

result = 0
for i in range(t):
    result += t[i] * f(l + i) - l * f(r)
print(result % (10**9 + 7))
