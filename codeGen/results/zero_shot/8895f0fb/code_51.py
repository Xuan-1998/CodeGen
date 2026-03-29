import sys
input = lambda: int(sys.stdin.readline())

T = input()  # Number of test cases
for _ in range(T):
    N = input()  # Maximum number of digits in A and B
    total_carries = 0  # Initialize total carries for all pairs

    # Generate all possible pairs of A and B (up to N digits)
    for i in range(10**(N-1), 10**N):  # A
        for j in range(i, 10**N):  # B
            carry_count = 0  # Initialize carries for current pair
            a_str = str(i)  # Convert A to string
            b_str = str(j)  # Convert B to string

            # Calculate the number of carries for this pair
            for k in range(N):
                if int(a_str[-1-k]) + int(b_str[-1-k]) >= 10:
                    carry_count += 1

            total_carries += carry_count  # Add to total carries

    expected_carries = total_carries / (10**(2*N-2))  # Calculate expected value
    print(expected_carries)
