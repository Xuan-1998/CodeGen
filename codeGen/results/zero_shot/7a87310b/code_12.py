import sys

def count_matrices(n):
    total = 0
    for i in range((n+1)//2 + 1):  # iterate over possible values of 'a'
        j = n - i
        if (i * j) % 2 == 0:  # check if the determinant is positive
            total += 1
    return total

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(count_matrices(N))
