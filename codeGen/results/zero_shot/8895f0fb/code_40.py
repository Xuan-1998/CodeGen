import sys

def calculate_expected_carries(N):
    # Calculate the total number of possible pairs for N-digit numbers
    total_pairs = 10**N
    
    # Initialize the sum of non-zero carries
    sum_non_zero_carry = 0
    
    for i in range(1, 10):  # Loop through each digit (1-9)
        for j in range(i+1, 10):  # Loop through each possible digit in B (i+1 to 9)
            # Calculate the number of non-zero carries when adding A and B
            carry_count = sum(1 for a, b in zip(map(int, str(i*a + i)), map(int, str(j*b + j))) if int(a) + int(b) >= 10)
            
            # Add the number of non-zero carries to the total sum
            sum_non_zero_carry += carry_count
    
    # Calculate the expected value by dividing the sum of non-zero carries by the total number of possible pairs
    expected_carries = sum_non_zero_carry / total_pairs
    
    return expected_carries

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(calculate_expected_carries(N))
