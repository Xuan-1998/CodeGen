import sys

def simulate_program(a):
    x, y = 1, 0
    while True:
        if x <= 0 or x > len(a):
            break
        x += a[x]
        y += a[x]
        x -= a[x]
        y += a[x]
    return y

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for i in range(n-1):
    print(simulate_program(a))
