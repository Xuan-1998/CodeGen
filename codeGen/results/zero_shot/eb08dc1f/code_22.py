python
# Step 1: Understand the problem
n = int(input())  # input integer n
blocks = [0] * (n + 1)  # initialize count of blocks for each length

# Step 2: Generate all integers from 0 to 10^n - 1 and pad with leading zeroes
for i in range(10**n):
    num_str = format(i, 'b').zfill(n)  # binary representation as a string, padded with zeros
    digit_counts = [0] * (n + 1)  # initialize count of digits for each length

    # Step 3: Count the number of blocks of each length in the current integer
    j = 0
    while j < n:
        k = j
        while k < n and num_str[k] == num_str[j]:
            k += 1
        digit_counts[k - j + 1] += 1
        j = k

    # Step 4: Update the count of blocks for each length in the overall result
    for i, count in enumerate(digit_counts):
        blocks[i] = (blocks[i] + count) % 998244353

# Step 5: Print the count of blocks of each length, modulo 998244353
print(*blocks, sep=' ')
