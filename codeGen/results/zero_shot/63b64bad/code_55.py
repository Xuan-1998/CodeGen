code
import sys
n = int(input())
sequence = list(map(int, input().split()))
output = []

for i in range(2, n+1):
    x, y = 1, 0
    while True:
        if x <= 0 or x > i:
            output.append(-1)
            break
        a_x = sequence[x-1]
        x += a_x
        y += a_x
        y -= a_x
    print(y)

sys.stdout.flush()
