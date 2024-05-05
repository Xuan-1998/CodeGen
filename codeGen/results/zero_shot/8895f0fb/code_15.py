import sys

def calculate_expected_carries():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        
        total_pairs = 10 ** (N - 1) * (9 + 2)  # Calculate the total number of pairs
        
        expected_carries = 0
        
        for i in range(N):
            carry_prob = (5 + i) / 10  # Probability of a digit being 1 or more
            no_carry_prob = 1 - carry_prob
            
            expected_no_carry = (no_carry_prob ** N) * (10 ** i)
            expected_carry = (carry_prob ** N) * (9 ** i)
            
            expected_carries += expected_carry / total_pairs
        
        print(expected_carries)

calculate_expected_carries()
