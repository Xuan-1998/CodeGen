n = int(input())
numbers = [str(i).zfill(n) for i in range(10**n)]
block_counts = {}
for num in numbers:
    for i in range(len(num)):
        block_start = i
        while i < len(num) and num[i] == num[block_start]:
            i += 1
        if i > block_start:
            block_length = i - block_start
            block_counts[block_length] = block_counts.get(block_length, 0) + 1

print(*[block_counts.get(i, 0) for i in range(1, n+1)], sep=' ')
