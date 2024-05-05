def expected_carries(N):
    carry_counts = [0] * (N + 1)
    for i in range(10 ** N):
        a = str(i).zfill(N)
        b = str(i ^ ((1 << N) - 1)).zfill(N)
        carry_count = sum(int(digit_a) + int(digit_b) >= 10 for digit_a, digit_b in zip(a, b))
        carry_counts[N] += carry_count
    return sum(carry_counts[:]) / (10 ** (2 * N))

T = int(input())
for _ in range(T):
    N = int(input())
    print(expected_carries(N))
