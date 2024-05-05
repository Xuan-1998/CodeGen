import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

result = []
for i in range(1, n+1):
    x, y = 1, 0
    while True:
        if x <= 0 or x > n:
            break
        x += sequence[x]
        y += sequence[x]
        x -= sequence[x]
    result.append(y)

for value in result:
    print(value if value >= 0 else -1)
