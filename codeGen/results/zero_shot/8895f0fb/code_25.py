# Read input
T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())  # Maximum number of digits in A and B
    
    # Initialize total carries and total pairs counters
    total_carries = 0
    total_pairs = 0
    
    # Generate all possible pairs of A and B with N digits
    for i in range(10**N):
        for j in range(i, 10**N):
            a = int(str(i) + str(j))  # Create A as the concatenation of i and j
            b = int(str(j) + str(i))  # Create B as the concatenation of j and i
            
            # Calculate the number of carries when adding A and B
            carry_count = 0
            temp_a, temp_b = a, b
            while temp_a > 0 and temp_b > 0:
                temp_a //= 10
                temp_b //= 10
                if (temp_a % 10) + (temp_b % 10) >= 10:
                    carry_count += 1
            carry_count += temp_a or temp_b
            
            # Increment total carries and total pairs counters
            total_carries += carry_count
            total_pairs += 1
    
    # Calculate the expected number of non-zero carries
    expected_carries = total_carries / total_pairs
    
    # Print the result
    print(expected_carries)
