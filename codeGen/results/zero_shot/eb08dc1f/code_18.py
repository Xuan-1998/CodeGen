n = int(input())
numbers = []
for i in range(10**n):
    num = str(i).zfill(n)
    numbers.append(num)

block_counts = {}
for num in numbers:
    for i in range(len(num)):
        digit = num[i]
        if digit not in block_counts:
            block_counts[digit] = 1
        else:
            block_counts[digit] += 1

block_lengths = sorted(block_counts.keys())

answer = [0] * n
for block_len in range(1, n+1):
    for digit in block_lengths:
        count = (block_counts[digit] // (10 ** (n - block_len))) % 998244353
        answer[block_len-1] += count

print(*answer, sep=' ')
