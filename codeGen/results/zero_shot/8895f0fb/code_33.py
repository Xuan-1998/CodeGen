import sys

def expected_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        total_pairs = 10**2*N
        total_carry_count = 0
        
        # Generate all possible pairs of A and B
        for a in range(10**N):
            for b in range(a, 10**N):
                carry_count = 0
                
                # Add the numbers and count the number of carries
                while a > 0 or b > 0:
                    a_digit = a % 10
                    b_digit = b % 10
                    
                    if a_digit + b_digit >= 10:
                        carry_count += 1
                    a //= 10
                    b //= 10
                
                total_carry_count += carry_count
        
        # Calculate the expected number of non-zero carries for all pairs
        expected_carries = total_carry_count / total_pairs
        
        print(f"{expected_carries:.6f}")

if __name__ == "__main__":
    expected_carries()
