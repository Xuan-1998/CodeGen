from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dp = defaultdict(lambda: -1)
dp[(1, 0)] = 0

for x in range(2, n+1):
    for y in range(max(a[:x])):
        if (x, y) in dp:
            continue
        a_val = a[x-1]
        new_x = x + a_val
        new_y = y + a_val
        if new_x > n or new_y > max(a):
            dp[(new_x, new_y)] = -1
        else:
            dp[(new_x, new_y)] = dp[(x, y)]
        while x <= 0 or x > n:
            return -1
        for i in range(2):
            a_val = a[x-1]
            new_x = max(x-a_val, 0)
            new_y = y + a_val
            if (new_x, new_y) in dp:
                continue
            dp[(new_x, new_y)] = new_y

for i in range(2, n+1):
    print(dp.get((i, 0), -1))
