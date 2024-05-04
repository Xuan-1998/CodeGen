# Read the input
n = int(input())

# Initialize an array to store the count of blocks of each length, modulo 998244353
blocks_count = [0] * (n + 1)

# Loop through all numbers from 0 to 10^n - 1
for i in range(10**n):
    # Convert the number to a string and find its length
    num_str = str(i).zfill(n)
    
    # Find the count of blocks of each length in the current number
    for j in range(1, n + 1):
        if (j == len(num_str)) or (num_str[j-1] != num_str[j]):
            blocks_count[j] += 1

# Print the result, modulo 998244353
for i in range(n+1):
    print((blocks_count[i]) % 998244353, end=' ')
