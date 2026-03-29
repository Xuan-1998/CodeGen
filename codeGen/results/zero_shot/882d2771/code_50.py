import sys

def read_input():
    t, l, r = map(int, input().split())
    return t, l, r

t, l, r = read_input()

# calculate f(l), f(l + 1), ..., f(r)
f_values = []
for i in range(l, r + 1):
    # this is where you would implement the function to calculate f(i)
    pass
    f_values.append(f(i))

total = 0
for i in range(t):
    total += i * f_values[i]

print((total - l * f_values[-1]) % (10**9 + 7))
