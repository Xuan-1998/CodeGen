from collections import defaultdict

def process_sequence(n):
    dp = defaultdict(int)
    for i in range(1, n+1):
        x, y = i, 0
        while x <= 0 or x > n:
            break
        while True:
            if (x, y) in dp:
                return dp[(x, y)]
            dp[(x, y)] = y
            x += a[x]
            y += a[x]
            x -= a[x]
            y += a[x]
    return -1

n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    print(process_sequence(i+2))
