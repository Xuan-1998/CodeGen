import sys

def calculate_expected_carry(N):
    total_pairs = (N+1)**(2*N)
    expected_carry = 0
    for i in range(N):
        carry_count = 0
        for j in range(N):
            if int(str(A)[i]) + int(str(B)[j]) >= 10:
                carry_count += 1
        expected_carry += carry_count / (N+1)**(2*N)
    return expected_carry

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    A, B = map(int, sys.stdin.readline().split())
    print(calculate_expected_carry(N))
