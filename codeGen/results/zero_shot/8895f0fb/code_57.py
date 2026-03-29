import sys
from itertools import product

def calculate_expected_carries(N):
    total_pairs = sum(range(1, N+2))
    
    expected_carries = 0
    
    for A in range(1, N+1):
        for B in range(A, N+1):
            carries = 0
            carry_over = 0
            
            for a_digit, b_digit in zip(map(int, str(A)), map(int, str(B))):
                sum_of_digits = a_digit + b_digit + carry_over
                if sum_of_digits >= 10:
                    carries += 1
                    carry_over = 1
                else:
                    carry_over = 0
                
            expected_carries += carries
    
    return expected_carries / total_pairs

T = int(input())
for _ in range(T):
    N = int(input())
    print(calculate_expected_carries(N))
