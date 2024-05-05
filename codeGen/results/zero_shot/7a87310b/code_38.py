import sys

def count_positive_invertible_matrices(n):
    count = 0
    for i in range(1, n+1):  # diagonal element
        for j in range(i+1, n+1):  # other diagonal element
            if (n - i) + (n - j) == n:  # condition for trace of N
                if (i * j) % ((n-i)*(n-j)) > 0:  # condition for positive determinant
                    count += 1
    return count

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(count_positive_invertible_matrices(N))
