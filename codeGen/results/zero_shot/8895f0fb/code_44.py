import sys

def calculate_expected_value():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        
        # Calculate the total number of pairs
        total_pairs = 10 ** (N - 1) * (9 + 10 ** N)
        
        expected_value = 0
        
        # Iterate over each digit in both numbers
        for _ in range(N):
            # Add the digits together and check if there is a carry
            if (10 ** _ - 1) * (9 + 10 ** (_ - 1)) >= 10:
                # If there is a carry, add up all possible values of the current digit
                expected_value += sum(range(10))
            else:
                # If there is no carry, add up all possible values of the current digit minus 1 (since one value is already counted)
                expected_value += sum(range(9)) + 1
        
        # Divide by the total number of pairs to get the expected value
        expected_value /= total_pairs
        
        print(expected_value)

calculate_expected_value()
