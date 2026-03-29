code
import sys

n = int(input())
sequence = list(map(int, input().split()))

for i in range(1, n):
    x = 1
    y = 0
    while True:
        if x <= 0 or x > i:
            break
        x += sequence[x]
        y += sequence[x]
        x -= sequence[x]

    print(y)
