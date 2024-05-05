import sys

def count_invertible_matrices(N):
    # Count the number of possible values for the non-diagonal elements
    count = 0
    for i in range(1, N // 2 + 1):
        if (N - 2 * i) % i == 0 and (N - 2 * i) // i > 0:
            count += 1

    return count

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(count_invertible_matrices(N))
