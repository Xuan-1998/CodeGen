import sys

def and_xor_count(n, k, arr):
    # Calculate the bitwise AND and XOR of all elements
    and_result = 0xffffffffffffffff >> (k - 1)
    xor_result = sum(1 << (i.bit_length() - 1) for i in arr)

    # Count the arrays where the minimum value is greater than or equal to the number of different bits
    count = 0
    for i in range(n):
        and_mask = and_result & ((1 << k) - 1)
        if (arr[i] & and_mask) >= xor_result:
            count += 1

    return count % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(and_xor_count(n, k, arr))
