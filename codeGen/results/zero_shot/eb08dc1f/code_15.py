import sys

# Read input
n = int(sys.stdin.readline())

# Initialize dictionary to store frequency of each digit
digit_freq = {}

for i in range(10**n):
    num_str = str(i).zfill(n)
    
    for j, c in enumerate(num_str):
        if c not in digit_freq:
            digit_freq[c] = []
        digit_freq[c].append((j, j))

block_counts = [0]*(n+1)

for digits in digit_freq.values():
    max_length = 0
    for start, end in digits:
        length = end - start + 1
        block_counts[length] += 1
        if length > max_length:
            max_length = length

# Calculate the count modulo 998244353
block_counts = [str(count) for count in map(lambda x: pow(10, x-1, 998244353)*x%998244353, block_counts)]
print(' '.join(block_counts))
