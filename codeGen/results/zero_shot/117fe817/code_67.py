def solution():
    # Initialize the count of digit 1
    count = 0
    
    # Iterate from 0 to n (inclusive)
    for i in range(n + 1):
        # Convert the integer to a string to easily check each digit
        str_i = str(i)
        
        # Count the number of times '1' appears in the string representation of the integer
        count += str_i.count('1')
    
    return count

# Read input from stdin
n = int(input())

# Print the solution to stdout
print(solution())
