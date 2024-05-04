n = int(input())
nums = [str(i).zfill(n) for i in range(10**n)]
block_counts = [0] * (n + 1)
for num in nums:
    length = len(num)
    block_start = 0
    while block_start < length:
        block_end = block_start
        while block_end < length and num[block_end] == num[block_start]:
            block_end += 1
        block_counts[block_end - block_start + 1] += 1
        block_start = block_end + 1
print(*[str(count) for count in block_counts], sep=' ')
