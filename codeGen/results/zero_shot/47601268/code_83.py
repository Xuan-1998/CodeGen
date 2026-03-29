# Step 1: Read input
n = int(input())

# Step 2: Initialize count of numbers without consecutive ones
count = 0

# Step 3: Loop through all numbers from 0 to n (inclusive)
for i in range(n + 1):
    # Step 4: Convert the number to binary and remove leading zeros
    binary_str = bin(i)[2:]

    # Step 5: Check if the binary string has consecutive ones
    has_consecutive_ones = False
    for j in range(len(binary_str) - 1):
        if binary_str[j] == '1' and binary_str[j + 1] == '1':
            has_consecutive_ones = True
            break

    # Step 6: If the binary string does not have consecutive ones, increment count
    if not has_consecutive_ones:
        count += 1

# Step 7: Print the result
print(count)
