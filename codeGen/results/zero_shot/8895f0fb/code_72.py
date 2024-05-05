import sys

def calculate_expected_carries(N):
    total_carry = 0
    total_pairs = 0
    for i in range(10**N):
        for j in range(i, 10**N):
            carry = sum((int(digit1) + int(digit2)) >= 10 for digit1, digit2 in zip(str(i)[::-1], str(j)[::-1])) - (N > 0)
            total_carry += carry
            total_pairs += 1
    return total_carry / total_pairs

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(calculate_expected_carries(N))
