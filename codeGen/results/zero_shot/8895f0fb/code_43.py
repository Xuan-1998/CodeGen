import sys

def calculate_expected_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        total_pairs = 10 ** (N - 1) * 9  # each pair has a unique combination of digits
        expected_carries = 0.0

        for digit in range(N):  # iterate over each digit position
            if digit == 0:  # units digit
                probability = (5 <= 10 ** N - 1) / total_pairs  # at least one input number has a units digit >= 5
            else:
                probability = sum(10 ** i <= A // 10 ** (N - 1 - i) for i in range(N)) / total_pairs

            expected_carries += probability

        print(f"{expected_carries:.6f}")  # print the result with 6 decimal places

calculate_expected_carries()
