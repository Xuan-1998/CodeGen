n = int(input())
sequence = list(map(int, input().split()))
results = [0] * (n - 1)

for i in range(1, n):
    x, y = 1, 0
    while x > 0 and x <= n:
        x += sequence[x]
        y += sequence[x]
        x -= sequence[x]
    results[i - 1] = y if x <= 0 else -1

for result in results:
    print(result)
