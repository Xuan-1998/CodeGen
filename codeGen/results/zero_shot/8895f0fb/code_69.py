code
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    expected_carries = 0
    
    # Generate all possible pairs of N-digit numbers A and B
    for i in range(10**(N-1), 10**N):
        for j in range(i, 10**N):
            a, b = str(i), str(j)
            
            # Calculate the number of carries when adding A and B
            carries = 0
            carry_over = 0
            result = ''
            for digit_a, digit_b in zip(reversed(a), reversed(b)):
                total = int(digit_a) + int(digit_b) + carry_over
                if total >= 10:
                    carries += 1
                    result = '1' + result
                    carry_over = 1
                else:
                    result = str(total % 10) + result
                    carry_over = 0
            
            # Add the number of carries for this pair to the expected value
            if carry_over > 0:
                expected_carries += 1
    
    # Print the expected value for this test case
    print(expected_carries / ((10**(2*N)) - (10**(N-1))) * (9**N))
