def count_digit_one(n):
    # Initialize the total count of digit 1
    total_count = 0
    
    # Iterate over all numbers from 0 to n (inclusive)
    for i in range(n + 1):
        # Convert the number into a string to easily get its digits
        num_str = str(i)
        
        # Count the occurrences of digit 1 in the current number
        count = num_str.count('1')
        
        # Add the count to the total count
        total_count += count
    
    return total_count

n = int(input())
print(count_digit_one(n))
