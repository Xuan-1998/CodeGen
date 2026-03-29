# Read inputs
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    # Convert integer to string to easily manipulate digits
    num_str = str(n)
    
    # Initialize count of unique digits
    unique_digits_count = 0
    
    # Initialize a set to keep track of visited digits
    visited_digits = set()
    
    for _ in range(m):
        new_num_str = ''
        
        # Iterate over each digit in the number
        for digit in num_str:
            # Calculate the successor of the current digit
            next_digit = str(int(digit) + 1)
            
            # If this is a new digit, increment count and add to set
            if next_digit not in visited_digits:
                unique_digits_count += 1
                visited_digits.add(next_digit)
            
            # Add the successor of the current digit to the new number string
            new_num_str += next_digit
        
        # Update the number for the next iteration
        num_str = new_num_str
    
    # Print the length of the resulting number modulo 10^9+7
    print(len(str(n)) + unique_digits_count) % (10**9 + 7)
