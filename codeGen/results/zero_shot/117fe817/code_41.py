def findCountOfOnes(n):
    # Initialize the count of 1s
    count = 0
    
    # Iterate over each integer from 0 to n
    for i in range(n + 1):
        # Convert the integer to a binary string and remove the '0b' prefix
        bin_str = bin(i)[2:]
        
        # Count the number of '1's in the binary string
        count += bin_str.count('1')
    
    return count

# Read input from stdin
n = int(input())

# Print the output to stdout
print(findCountOfOnes(n))
