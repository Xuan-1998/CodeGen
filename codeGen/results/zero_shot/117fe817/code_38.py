def count_digit_ones(n):
    # Initialize the total count of digit 1s
    total_count = 0
    
    # Count the number of times the digit 1 appears at the beginning of numbers up to n
    for i in range(1, n+1):
        if str(i).startswith('1'):
            total_count += len(str(i)) - 1
    
    # Count the number of times the digit 1 appears within numbers up to n
    for i in range(10, n+1):
        total_count += (i // 10) * (len(str(i)) - 2)
    
    return total_count

n = int(input())  # Read input from stdin
print(count_digit_ones(n))  # Print the result to stdout
