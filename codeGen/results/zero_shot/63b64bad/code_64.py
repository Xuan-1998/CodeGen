import sys

n = int(input())
sequence = list(map(int, input().split()))
output = []

for a in sequence:
    x, y = 1, 0
    while True:
        if x <= 0 or x > n:
            output.append(-1)
            break
        x += a
        y += a
        x -= a
    else:
        output.append(y)

print(*output, sep='\n')
