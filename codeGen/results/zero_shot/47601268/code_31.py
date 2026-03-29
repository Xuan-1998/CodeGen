# Receive input from standard input
n = int(input())

# Initialize count variable to store the number of integers that do not have consecutive ones in their binary representation
count = 0

# Iterate over all numbers from 0 to n (inclusive)
for i in range(n + 1):
    # Convert the integer to a binary string and remove the '0b' prefix
    binary_str = bin(i)[2:]
    
    # Initialize flag to track whether consecutive ones were found
    consecutive_ones_found = False
    
    # Iterate over all characters in the binary string
    for j in range(len(binary_str)):
        if j > 0 and binary_str[j] == '1' and binary_str[j - 1] == '1':
            consecutive_ones_found = True
            break
        
    # If no consecutive ones were found, increment the count
    if not consecutive_ones_found:
        count += 1

# Print the final count to standard output
print(count)
