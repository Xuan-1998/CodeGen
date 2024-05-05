import sys
from collections import defaultdict

# Read input
t = int(input())
mod = 10**9 + 7

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # Step 1: Calculate bitwise AND of all elements
    and_result = reduce(lambda x, y: x & y, arr)

    # Step 2: Count arrays for which the result of bitwise AND is greater than or equal to bitwise XOR
    count = 0

    for bits in range(2**k):
        # Calculate bitwise XOR of all elements with the current bits set
        xor_result = reduce(lambda x, y: x ^ y, [bits | bit for bit in arr])

        if (and_result >= xor_result):
            count += 1

    print(count % mod)
