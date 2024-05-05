import sys

def count_positive_invertible_matrices(n):
    # TO DO: Implement the logic here!
    pass

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    result = count_positive_invertible_matrices(n)
    print(result)

