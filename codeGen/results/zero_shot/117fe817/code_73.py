def findDigitOneCount(n):
    # Calculate the number of integers less than or equal to n
    total_count = 0
    
    for i in range(n + 1):
        # Convert i to a string and count the occurrences of '1'
        str_i = str(i)
        ones_in_i = str_i.count('1')
        
        # Add this count to our running total
        total_count += ones_in_i
    
    return total_count

n = int(input())  # Read n from standard input
print(findDigitOneCount(n))  # Print the result to standard output
