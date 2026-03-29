import sys

def simulate_program(a):
    x = y = 1
    while 1 <= x <= len(a) and x > 0:
        x += a[x]
        y += a[x]
        x -= a[x]
    return y if 1 <= x <= len(a) else -1

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    print(simulate_program(a))
