import sys

# Read input from stdin
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    
    # Initialize carries and total_pairs
    carries = 0
    total_pairs = 1
    
    # Iterate through each digit of A and B
    for i in range(N):
        # Calculate the maximum value that can be added to the current digit without a carry
        max_addition = 10 ** (N - i - 1) - 1
        
        # Calculate the number of carries from this digit
        if i == 0:
            carries += sum(1 for j in range(max_addition + 1) if (A % 10 + B % 10) // 10 >= max_addition)
        else:
            carries += sum(1 for j in range(max_addition + 1) if ((A % 10 + B % 10) // 10) >= max_addition)
        
        # Update the total number of pairs
        total_pairs *= (max_addition + 1)
    
    # Calculate the expected value and print it to stdout
    expected_value = carries / total_pairs
    print(expected_value)
