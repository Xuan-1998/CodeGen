while m > 0:
    # Convert n to a list of digits
    digits = [int(d) for d in str(n)]
    
    # Apply the operation: replace each digit with its successor
    new_digits = [(d + 1) % 10 for d in digits]
    
    # Convert the new list of digits back to an integer
    n = int(''.join(map(str, new_digits)))
    
    # Decrement m by 1
    m -= 1
    
# Print the length of the resulting number modulo 10^9+7
print(len(str(n)) % (10**9 + 7))
