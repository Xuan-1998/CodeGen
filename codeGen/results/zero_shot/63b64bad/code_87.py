import sys

def simulate_program(a):
    x = 1
    y = 0
    while True:
        x += a[x]
        y += a[x]
        if x <= 0 or x > len(a):
            return y
        x -= a[x]

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for i in range(len(a)):
    result = simulate_program(a)
    print(result) if result != -1 else print(-1)
