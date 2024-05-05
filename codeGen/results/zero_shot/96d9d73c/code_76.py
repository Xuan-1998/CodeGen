import sys

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

p = 0
for i in range(1, n):
    if a[i] - a[p] > m:
        p += 1
        if a[i] - a[p] <= m and i - p >= k:
            continue
        else:
            print("false")
            sys.exit()

print("true" if (n - p) >= k else "false")
