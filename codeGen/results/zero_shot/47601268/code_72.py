def no_consecutive_ones(num):
    bin_num = bin(num)[2:]  # Convert num to binary and remove '0b' prefix
    for i in range(len(bin_num) - 1):  # Iterate through the binary string
        if bin_num[i] == '1' and bin_num[i + 1] == '1':
            return False  # If consecutive ones are found, return False
    return True  # If no consecutive ones are found, return True

# Code block starts here
def count_numbers(n):
    count = 0
    for i in range(n + 1):  # Iterate through numbers from 0 to n
        if no_consecutive_ones(i):  # Check if the binary representation has consecutive ones
            count += 1  # If not, increment the count

    print(count)  # Print the final count

# Receive input and call the function
n = int(input())
count_numbers(n)
