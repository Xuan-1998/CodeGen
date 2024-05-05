import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

results = []
for i in range(2, n+1):
    x = 1
    y = 0
    while True:
        if x <= 0 or x > i:
            break
        x += sequence[i-1]
        y += sequence[i-1]
        x -= sequence[i-1]
        y += sequence[i-1]
    results.append(y)

for result in results:
    print(result)
