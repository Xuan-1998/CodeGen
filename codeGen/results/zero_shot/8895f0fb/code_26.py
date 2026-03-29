import sys

def calculate_expected_carry(N):
    total_pairs = N * (N + 1)
    expected_value = 0.0
    
    for i in range(10**N):
        a = str(i).zfill(N)
        carry_count = 0
        
        for j in range(N):
            sum_digit = int(a[j]) + int((str(i) + str(10**(N-1-j))).zfill(N)[j])
            if sum_digit >= 10:
                carry_count += 1
        
        expected_value += carry_count / total_pairs
    
    return expected_value

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(calculate_expected_carry(N))
