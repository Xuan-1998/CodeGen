import sys

def solve(n, m):
    # Calculate the maximum value
    max_val = n + m

    # Calculate the length of the resulting number
    len_res = max_val.bit_length()

    return len_res % (10**9 + 7)

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(solve(n, m))
