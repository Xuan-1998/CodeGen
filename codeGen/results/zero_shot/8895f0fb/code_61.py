T = int(input())
for _ in range(T):
    N = int(input())
    total_pairs = N * (N + 1) // 2
    carry_per_digit = (10 - 1) / 10
    expected_carry = total_pairs * carry_per_digit
    print(f"{expected_carry:.6f}")
