import sys

def and_xor_count(n, k):
    total_and = 0
    total_xor = 0
    for i in range(2**k-1):
        and_temp = 0
        xor_temp = 0
        for j in range(n):
            and_temp |= (i >> j) & 1
            xor_temp ^= (i >> j) & 1
        total_and += and_temp
        total_xor += xor_temp
    return ((total_and + 1) * (total_and + 2)) // 2 - ((total_xor + 1) * (total_xor + 2)) // 2

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    print(and_xor_count(n, k) % (10**9+7))
