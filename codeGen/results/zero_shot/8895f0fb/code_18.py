import math

def num_pairs(N):
    return math.comb(10**N, 10**N)

def add_numbers(A, B):
    result = 0
    carry = 0
    for i in range(N-1, -1, -1):
        digit_A = int(str(A)[i])
        digit_B = int(str(B)[i])
        total = digit_A + digit_B + carry
        if total >= 10:
            result += 1
            carry = 1
        else:
            carry = 0
    return result

def expected_carries(N):
    total_pairs = num_pairs(N)
    total_carry_count = 0
    for _ in range(total_pairs):
        A = int(input())  # read A from stdin
        B = int(input())  # read B from stdin
        carry_count = add_numbers(A, B)
        total_carry_count += carry_count
    return total_carry_count / total_pairs

T = int(input())  # read T from stdin

for _ in range(T):
    N = int(input())  # read N from stdin
    print(expected_carries(N))
