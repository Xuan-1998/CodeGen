import sys
T = int(input())  # Read T from stdin

for _ in range(T):
    N = int(input())  # Read N from stdin
    
    A_max, B_max = 10**N - 1, 10**N - 1  # Calculate the maximum values of A and B
    total_carries = 0
    
    for i in range(1, 10):  # For each digit (1-9)
        A_count, B_count = 0, 0
        
        for j in range(i):  # For each value of the current digit in A (0-i-1)
            for k in range(i):  # For each value of the current digit in B (0-i-1)
                if j + k >= i:  # If adding j and k results in a sum greater than or equal to i
                    total_carries += 1  # Increment the total number of carries
    
    expected_carries = total_carries / ((10**N)**2)  # Calculate the expected number of non-zero carries

    print(f"{expected_carries:.6f}")  # Print the expected number of non-zero carries to stdout
