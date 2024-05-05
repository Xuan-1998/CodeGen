import math
from functools import lru_cache

@lru_cache(None)
def C(n, k):
    return math.comb(n, k)

n = int(input())
mod = 998244353
total_prob = 0

for i in range(1 << n):  # iterate over all subsets of {0, 1, ..., n-1}
    ones_count = bin(i).count('1')  # count the number of towns that will get signal
    if ones_count == 1:  # we only need to consider sets with exactly one town getting signal
        total_prob += C(n - 1, ones_count) * C(ones_count, 0)
print(total_prob % mod)
