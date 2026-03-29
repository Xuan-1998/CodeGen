import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

def simulate_program(sequence):
    y = 0
    x = 1
    for a in sequence:
        x += a
        y += a
        y += a - (x % a)
    return y

for i in range(1, n+1):
    print(simulate_program(range(i, n+1)))
