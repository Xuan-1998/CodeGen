import sys

def calculate_expected_carries(N):
    T = int(sys.stdin.readline())
    expected_carries = 0.0
    for _ in range(T):
        N = int(sys.stdin.readline())
        carries = 0
        for i in range(10**N):
            A = str(i)
            for j in range(i+1, 10**N):
                B = str(j)
                carry_count = 0
                for k in range(N):
                    sum_of_digits = int(A[k]) + int(B[k])
                    if sum_of_digits >= 10:
                        carry_count += 1
                carries += carry_count
        expected_carries += carries / (10**N)**2
    return expected_carries / T

print(calculate_expected_carries(int(sys.stdin.readline())))
