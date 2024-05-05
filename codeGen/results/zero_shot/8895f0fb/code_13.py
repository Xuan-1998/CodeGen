import sys

def calculate_expected_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        total_carries = 0
        for i in range(N):
            carries_per_pair = 0
            for j in range(10):
                a = (i + 1) * 10 ** (N - 1)
                b = (j + 1) * 10 ** (N - 1)
                sum_digits = sum(int(digit) for digit in str(a + b))
                carries_per_pair += int(sum_digits >= 10)
            total_carries += carries_per_pair
        expected_total_carries = total_carries / (T * N * (N + 1) // 2)
        print(expected_total_carries)

calculate_expected_carries()
