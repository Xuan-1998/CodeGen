import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    total_ways = 1
    for i in range(m):
        if i % 2 == 0:
            total_ways *= (n // 2 + 1)
        else:
            if i < n/2:
                total_ways *= (n // 2 + 1)
            else:
                total_ways *= (n - i)
    print(total_ways % (10**8+7))
