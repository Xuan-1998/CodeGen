import sys

def simulate_sequence(a):
    x = 1
    y = 0
    while True:
        if x <= 0 or x > len(a):
            return y
        x += a[x]
        y += a[x]
        x -= a[x]

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for i in range(n-1):
    print(simulate_sequence(a[i+2:]))
