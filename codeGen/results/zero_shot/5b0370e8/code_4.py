import sys

def test_case():
    n, k = map(int, input().split())
    and_result = (1 << k) - 1
    xor_result = 0

    for _ in range(n):
        x = int(input())
        and_result &= x
        xor_result ^= x

    count = 0
    for a in range(2**k):
        if ((a & and_result) >= a) and (xor_result & a == 0):
            count += 1

    print(count % (10**9 + 7))

test_case()
