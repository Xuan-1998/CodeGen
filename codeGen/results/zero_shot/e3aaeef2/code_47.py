import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    count_digits = lambda x: len(str(x))
    result_length = 0
    for _ in range(m):
        n = sum(int(d) + 1 for d in str(n))
        result_length += (count_digits(n) - count_digits(n-1)) % 2
    print(result_length % (10**9+7))
