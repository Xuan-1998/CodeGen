import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    A = int(input(f"Enter {N}-digit number A: "))
    B = int(input(f"Enter {N}-digit number B: "))
    carries = 0
    for i in range(N):
        digit_sum = (A // 10**i) % 10 + (B // 10**i) % 10
        if digit_sum >= 10:
            carries += 1
    expected_carries = carries / (N * (N + 1) // 2)
    print(f"{expected_carries:.6f}")
