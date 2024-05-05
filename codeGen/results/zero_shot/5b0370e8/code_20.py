import sys

def solve(n, k):
    mod = 10**9 + 7
    result = 0
    for mask in range(2**k - 1):
        and_count = 0
        xor_count = 0
        for num in range(n):
            if (num & mask) > 0:
                and_count += 1
            xor_count ^= num & mask
        result += (and_count >= 1) & (xor_count >= 1)
    return result % mod

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
