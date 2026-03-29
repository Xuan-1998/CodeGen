import sys

def simulate_program(a, n):
    x = y = 1
    result = -1
    while True:
        x += a[x]
        y += a[x]
        if x <= 0 or x > n:
            result = y
            break
    return result

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    print(simulate_program(a, i))
