import sys
from collections import defaultdict

n, k, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

a.sort()

partitions = 0
prev = a[0]
diff = 1

for x in a:
    if x - prev > m:
        partitions += 1
        prev = x
    diff = min(diff, x - prev)

if len(a) % k == 0 and diff >= (a[-1] - a[0]) // k:
    print(True)
else:
    print(False)
