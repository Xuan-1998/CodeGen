import sys

# Read input
t, l, r = map(int, input().split())

def f(n):
    # Your implementation for calculating f(n) goes here
    pass  # Replace with your actual solution

res = 0
for i in range(l, r+1):
    res += t * f(i) - l * f(r)
    res %= 10**9 + 7

print(res)
