import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

for i in range(1, n+1):
    x = 1
    y = 0
    while True:
        if x <= 0 or x > n:
            break
        a_i = sequence[x-1]
        x += a_i
        y += a_i
        x -= a_i
    print(y)
