import sys

def calculate_expected_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        A_max, B_max = 10**N - 1, 10**N - 1
        total_pairs = (A_max + 1) * (B_max + 1)
        carries_sum = 0
        for a in range(A_max + 1):
            for b in range(B_max + 1):
                carry_count = 0
                carry_over = 0
                for digit_a, digit_b in zip(map(int, str(a)), map(int, str(b))):
                    sum_digit = digit_a + digit_b + carry_over
                    if sum_digit >= 10:
                        carry_count += 1
                        carry_over = 1
                    else:
                        carry_over = 0
                carries_sum += carry_count
        expected_carries = carries_sum / total_pairs
        print(expected_carries)

calculate_expected_carries()
