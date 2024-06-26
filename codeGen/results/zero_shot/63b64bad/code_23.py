import sys

def simulate_program(a):
    x, y = 1, 0
    while True:
        if x <= 0 or x > len(a):
            return y
        x += a[x]
        y += a[x]
        x -= a[x]

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    print(simulate_program(list(range(i+2))))
