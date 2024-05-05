python
def count_binary_non_consecutive_ones(n):
    # Step 1: Initialize the count of non-negative integers with no consecutive ones
    count = 0
    
    # Step 2: Iterate over all numbers from 0 to n (inclusive)
    for i in range(n + 1):
        # Step 3: Convert the binary representation of the current number to a string
        binary_str = bin(i)[2:]
        
        # Step 4: Check if the binary string contains consecutive ones
        has_consecutive_ones = False
        consecutive_one_count = 0
        for j in range(len(binary_str) - 1):
            if binary_str[j] == '1' and binary_str[j + 1] == '1':
                consecutive_one_count += 1
                if consecutive_one_count > 1:
                    has_consecutive_ones = True
                    break
            else:
                consecutive_one_count = 0
        
        # Step 5: If the binary string does not contain consecutive ones, increment the count
        if not has_consecutive_ones:
            count += 1
    
    return count

n = int(input())  # Receive input from stdin
print(count_binary_non_consecutive_ones(n))  # Print the answer to stdout
