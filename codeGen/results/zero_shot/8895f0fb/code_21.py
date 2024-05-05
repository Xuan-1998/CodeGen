import sys

def calculate_expected_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        total_pairs = 1
        for i in range(N - 1):
            total_pairs *= (10 ** (N - i - 1))
        total_non_zero_carry = 0
        for a in range(10 ** N):
            for b in range(10 ** N):
                carry_count = 0
                sum_digits = [int(d) for d in str(a + b)]
                for digit in sum_digits:
                    if digit >= 10:
                        carry_count += 1
                total_non_zero_carry += carry_count
        expected_carries = total_non_zero_carry / (total_pairs * total_pairs)
        print(expected_carries)

calculate_expected_carries()
