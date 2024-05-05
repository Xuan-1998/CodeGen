code_block
T = int(input())
for _ in range(T):
    N = int(input())
    total_pairs = N * (N + 1) // 2
    carry_count = 0
    for i in range(N):
        a_digit = int(str(10**i)[1])
        b_digit = int(str(10**(N-1-i))[1])
        if a_digit + b_digit >= 10:
            carry_count += 1
expected_carry = carry_count / total_pairs
print(expected_carry)
closing_code_block
