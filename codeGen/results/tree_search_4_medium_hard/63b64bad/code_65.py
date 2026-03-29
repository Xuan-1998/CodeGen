from collections import defaultdict
dp = defaultdict(int)

n = int(input())
sequence = list(map(int, input().split()))

for x in range(1, n+1):
    while True:
        if sequence[x-1] <= 0 or sequence[x-1] > n:
            break
        new_x = x + sequence[x-1]
        new_y = y + sequence[x-1]
        dp[(new_x, new_y)] = max(dp.get((x, y), y) + sequence[x-1], dp.get((new_x, new_y), 0))
        x, y = new_x, new_y
print(dp.get((n-1, 0), -1))
