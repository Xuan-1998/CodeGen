import sys

def calculate_expected_carries(T, N):
    total_pairs = 10**N * (10**N - 1) // 2
    expected_carries = 0

    for _ in range(T):
        A = int(input())
        B = int(input())

        # Count non-zero carries when adding A and B
        carries = 0
        while A > 0 or B > 0:
            a_digit = A % 10
            b_digit = B % 10

            if a_digit + b_digit >= 10:
                carries += 1
            A //= 10
            B //= 10

        expected_carries += carries / total_pairs

    print(expected_carries)
