import sys
from collections import defaultdict

def count_arrays(n, k, arr):
    dp = [0] * (1 << k)
    memo = defaultdict(int)

    for i in range(2**k - 1, -1, -1):
        and_result = i
        xor_result = 0
        count = 0

        for j in range(n):
            if ((and_result >> arr[j]) & 1) == 0:
                and_result &= ~(1 << arr[j])
            else:
                and_result |= (1 << arr[j])

            xor_result ^= arr[j]
            if and_result >= (1 << k) - 1:
                count = i + 1
                break

        memo[(and_result, xor_result)] = (memo.get((and_result, xor_result), 0) + count) % (10**9 + 7)

    return memo[(0, 0)]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_arrays(n, k, arr))
