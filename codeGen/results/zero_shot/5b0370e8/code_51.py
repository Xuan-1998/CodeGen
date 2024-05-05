import sys
from functools import reduce

def solve(n, k, arr):
    and_result = reduce(lambda x, y: x & y, arr)
    xor_result = reduce(lambda x, y: x ^ y, arr)

    count = 0
    for i in range(2**k):
        temp_and = i
        temp_xor = i
        for num in arr:
            temp_and &= num
            temp_xor ^= num
        if and_result >= xor_result:
            count += (temp_and >= xor_result) * ((1 << k) - 1)

    return count % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, k, arr))
