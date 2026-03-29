n = int(input())

numbers = []
for i in range(10**n):
    numbers.append(format(i, '0{}d'.format(n)))

from itertools import groupby

block_counts = {}
for key in '0123456789':
    blocks = (list(g) for k, g in groupby(numbers, str(key)))
    block_counts[key] = len(list(blocks))

result = [block_counts.get(str(d), 0) % 998244353 for d in '0123456789']
print(*result, sep=' ')
