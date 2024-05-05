# Read input
T = int(input())
for _ in range(T):
    N = int(input())
    
    # Calculate the total number of pairs possible for N-digit numbers
    total_pairs = (10**N) * (10**N)
    
    # Initialize the count of non-zero carries
    carry_count = 0
    
    # Iterate over all possible values of A and B
    for a in range(10**N):
        for b in range(10**N):
            # Calculate the sum of A and B
            sum_ab = a + b
            
            # Check if any digit of the sum is greater than or equal to 10
            carry = False
            while sum_ab > 0:
                digit_sum = sum_ab % 10
                sum_ab //= 10
                
                # If the digit is greater than or equal to 10, there's a carry
                if digit_sum >= 10:
                    carry = True
                    break
            
            # Increment the count of non-zero carries if there was one
            if carry:
                carry_count += 1
    
    # Calculate the expected number of non-zero carries and print it
    expected_carries = carry_count / total_pairs
    print(f"{expected_carries:.6f}")
