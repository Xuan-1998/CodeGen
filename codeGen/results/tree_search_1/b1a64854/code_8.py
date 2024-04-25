import sys
from math import gcd

def min_matrix_sum(N, M):
    return gcd(N, M)

# Read number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    N, M = map(int, input().strip().split())
    print(min_matrix_sum(N, M))
