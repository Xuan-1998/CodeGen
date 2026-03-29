import sys

n = int(input())
a = list(map(int, input().split()))
dp = {(1, 0): 0}

for x in range(2, n+1):
    last_x, last_y = (x-1), dp[(x-1, 0)]
    while x <= 0 or x > n:
        x -= a[x]
        y = last_y + a[x]
    dp[(x, y)] = y

print(*[dp.get((i+1, 0)) for i in range(n-1)], sep='\n')
