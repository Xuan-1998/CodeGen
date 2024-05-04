import sys

n = int(sys.stdin.readline())

# Generate all numbers from 0 to 10^n - 1
numbers = ['{:0{}d}'.format(i, n) for i in range(10**n)]

block_counts = [0] * (n + 1)

for num in numbers:
    # Find blocks of equal digits in the current number
    for length in range(1, n + 1):
        if len(set(num[i:i+length])) == 1:  # Check if all characters are the same
            block_counts[length] = (block_counts[length] + 1) % 998244353

# Print the count of blocks of each length
print(*block_counts, sep=' ')
