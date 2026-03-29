import sys

def expected_carries(N):
    total_pairs = 1
    for _ in range(1, N+1):
        total_pairs *= 10

    total_non_zero_carries = 0
    for i in range(1, 10):
        for j in range(i+1, 10):
            a = int(f"{i:0{N}d}")
            b = int(f"{j:0{N}d}")
            non_zero_carries = 0
            carry = 0
            while a and b:
                sum_digits = (a % 10) + (b % 10)
                if sum_digits >= 10:
                    non_zero_carries += 1
                    carry = 1
                a //= 10
                b //= 10
            total_non_zero_carries += non_zero_carries

    return total_non_zero_carries / total_pairs

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(expected_carries(N))
