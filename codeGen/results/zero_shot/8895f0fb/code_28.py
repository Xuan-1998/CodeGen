import sys

def expected_carries(T):
    total_carries = 0
    for _ in range(T):
        N = int(sys.stdin.readline())
        A = int(str(9 * (10 ** N - 1)) + '9' * N)
        B = int(str(9 * (10 ** N - 1)) + '9' * N)
        carries = sum(int(digit) >= 5 for pair in zip(map(int, str(A + B)), range(N)) for digit in map(str, pair))
        total_carries += carries
    return total_carries / T

T = int(sys.stdin.readline())
print(expected_carries(T))
