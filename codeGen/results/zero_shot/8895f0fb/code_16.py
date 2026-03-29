import sys

def calculate_expected_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        expected_carries = 0.0
        total_pairs = 1
        for i in range(N, 0, -1):
            total_pairs *= (i * 10 + 9)  # C(N, i)
            for j in range(i):
                carry_positions = [j]
                if len(carry_positions) > 0:
                    expected_carries += len(carry_positions)
        print(expected_carries / total_pairs)

calculate_expected_carries()
