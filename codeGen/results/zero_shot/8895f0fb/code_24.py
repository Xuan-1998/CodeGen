import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    total_pairs = (10 ** N) * (10 ** N)
    carries = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            a = int(f"{i:0{N}d}")
            b = int(f"{j:0{N}d}")
            carry_count = sum(int((a + b) // (10 ** k)) for k in range(N))
            carries += carry_count
    expected_carries = carries / total_pairs
    print(format(expected_carries, ".6f"))
