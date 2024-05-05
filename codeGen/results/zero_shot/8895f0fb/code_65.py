import sys

def expected_carries(T, N):
    # Initialize the count of carries
    carry_count = 0
    
    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        
        # Calculate the maximum value of A and B
        max_val = 10 ** (n - 1)
        
        # Generate all possible pairs of A and B
        for a in range(max_val + 1):
            for b in range(a, max_val + 1):
                # Count the number of carries when adding digits
                carry_count += sum(1 for d_a, d_b in zip(str(a)[::-1], str(b)[::-1]) if int(d_a) + int(d_b) >= 10)
        
        # Calculate the expected value by dividing by the total number of pairs
        expected_value = carry_count / (max_val * max_val)
    
    return round(expected_value, 6)

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    print(expected_carries(1, N))
