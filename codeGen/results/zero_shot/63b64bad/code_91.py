import sys

def simulate_program(a):
    x, y = 1, 0
    while True:
        if x <= 0 or x > len(a):
            return -1  # program terminates, return -1
        x += a[x]
        y += a[x]
        x -= a[x]
    return y

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    result = simulate_program(a[i:])
    print(result if result != -1 else -1)
