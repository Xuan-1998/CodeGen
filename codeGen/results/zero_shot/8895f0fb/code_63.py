import sys
from itertools import product

# Read input
T = int(input())
for _ in range(T):
    N = int(input())
    
    # Generate all possible pairs of A and B
    pairs = list(product(range(10**N), range(10**N)))
    
    # Initialize the count of non-zero carries
    carry_count = 0
    
    for pair in pairs:
        a, b = str(pair[0]), str(pair[1])
        
        # Perform addition and count non-zero carries
        carry = False
        result = ''
        for i in range(N-1, -1, -1):
            digit_sum = int(a[i]) + int(b[i])
            if digit_sum >= 10:
                carry = True
                result = '9' + result
            else:
                result = str(digit_sum) + result
        
        # If the most significant digit is also part of the carry, increment count
        if (int(a[0]) + int(b[0])) >= 10 and not carry:
            carry_count += 1
    
    # Calculate expected value by dividing total number of pairs by the count
    expected_value = carry_count / (len(pairs) * N)
    
    print(f'{expected_value:.6f}')
