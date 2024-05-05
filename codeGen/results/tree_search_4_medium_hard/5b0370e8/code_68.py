import sys

def count_arrays(n, k):
    and_result = 0
    xor_result = 0
    for i in range(n):
        # Update AND result using bit manipulation
        and_result &= (1 << k) - 1 if (xor_result & (1 << k) - 1) == 0 else xor_result

        # Update XOR result using two-pointer technique
        if (xor_result >> (k - 1)) == 0:
            xor_result = (xor_result << 1) | int(input().strip())
        else:
            xor_result ^= int(input().strip())

    return and_result >= (1 << k) - 1

t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    result = count_arrays(n, k)
    print(result % (10**9 + 7))
