import sys

def count_positive_invertible_matrices(n):
    count = 0
    for i in range(1, n+1):  # possible values for top-left element
        for j in range(i, n+1):  # possible values for bottom-right element
            if (i + j) % 2 == 0:  # ensure trace is even
                count += 1
    return count

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(count_positive_invertible_matrices(n))
