from itertools import groupby

n = int(input())
nums = [str(i).zfill(n) for i in range(10**n)]

block_counts = {}
for num in nums:
    for k, g in groupby(str(num)):
        block_count = len(list(g)) + 1  # Add 1 for the first and last digit if it's the same
        block_counts[block_count] = block_counts.get(block_count, 0) + 1

result = [pow(10, i, 998244353) * block_counts.get(i, 0) % 998244353 for i in range(n + 1)]
print(' '.join(map(str, result)))
