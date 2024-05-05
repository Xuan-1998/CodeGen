import random
import sys

n = int(sys.stdin.readline())

towers = [False] * (n + 2)

count = 0

for _ in range(2 ** n):
    for i in range(1, n + 1):
        towers[i] = random.choice([True, False])

    if (sum(towers[j] for j in range(1, n + 1)) == 1) and not any(towers[0] or towers[n + 1]):
        count += 1

print((count * 2 ** n) % 998244353)
