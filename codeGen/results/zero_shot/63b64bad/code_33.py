import sys

def simulate_program(a):
    x, y = 1, 0
    while True:
        if x <= 0 or x > len(a):
            return y
        a_x = a[x - 1]
        x += a_x
        y += a_x
        x -= a_x
    return -1

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]
for i, ai in enumerate(a):
    print(simulate_program([*range(2, n + 1), *a]))
