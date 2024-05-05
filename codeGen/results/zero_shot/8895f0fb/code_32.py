import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    expected_carry = 0
    for i in range(N):
        for j in range(i+1, N):
            # Calculate the sum of two digits from A and B
            sum_digit = (10**i) + (10**(N-1-j)) - 9
            if sum_digit >= 10:
                expected_carry += 1
    print(expected_carry / ((N*(N+1))/2))
