# Get the input n
n = int(input())

# Initialize an array of size n+1 with zeros
dp = [0] * (n + 1)

# For each number from 0 to 10^n - 1
for i in range(10**n):
    # Convert the number to a string, pad it with leading zeroes to length n
    num_str = format(i, 'b').zfill(n)
    
    # Initialize an index for the current number of blocks
    j = len(num_str[0])
    
    # Iterate over the digits in the number
    for digit in num_str:
        # If the current block has a different length than the previous one
        if len(digit) != j:
            # Update the index to reflect the new block starting here
            j = len(digit)
    
    # Increment the count of blocks of this length
    dp[j] += 1

# Calculate the count of each block size modulo 998244353
block_counts = [(dp[i] * (10**i)) % 998244353 for i in range(n + 1)]

# Print the answer
print(*block_counts, sep=' ')
