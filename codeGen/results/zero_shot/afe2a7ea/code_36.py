import sys
from math import comb

n = int(sys.stdin.readline())

total_configurations = 2 ** n
valid_configurations = sum(1 for _ in range(comb(n, k)) if (k == 0 or k == n) and all(k != i for i in range(1, n+1)))

probability = valid_configurations / total_configurations % 998244353

print(probability)
