import sys

def count_positive_invertible_matrices(n):
    count = 0
    for a in range(1, n//2 + 1):  # a can be positive or negative
        for d in range(a, n//2 + 1):  # d must have the same sign as a
            if (a * d) % n == 0:  # ensure ad is divisible by N
                continue
            b_values = set(range(-n//2, n//2 + 1))  # possible values of b
            for c in range(1, abs(n - 2*a)):  # c must have a different sign than a
                if (a * d) % n != (c * (-b or 0)) % n:  # ensure determinant is positive
                    continue
                count += 1
    return count

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(count_positive_invertible_matrices(N))
