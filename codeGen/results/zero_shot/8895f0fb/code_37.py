import sys
from itertools import product

def calculate_expected_carries(N):
    total_pairs = sum((10**n-1) * (10**(N-n)) for n in range(1, N+1))
    expected_carries = 0
    
    for a, b in product(range(10**N), range(10**N)):
        carry_count = 0
        while a and b:
            sum_digits = (a % 10) + (b % 10)
            if sum_digits >= 10:
                carry_count += 1
            a //= 10
            b //= 10
        
        expected_carries += carry_count
    
    return expected_carries / total_pairs

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(calculate_expected_carries(N))
