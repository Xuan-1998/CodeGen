import sys

def simulate_program(a):
    x = 1
    y = 0
    while x <= len(a) and x > 0:
        x += a[x]
        y += a[x]
        x -= a[x]
    return y if x > 0 else -1

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    print(simulate_program(a[i-1:i+1]))
