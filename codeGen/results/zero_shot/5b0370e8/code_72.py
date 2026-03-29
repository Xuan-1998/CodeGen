import sys

def f(x):
    res = 0
    for i in range(2**k):
        and_result = x
        xor_result = x
        for j in range(k):
            if (i >> j) & 1:
                and_result &= arr[j]
                xor_result ^= arr[j]
            else:
                and_result &= 0
                xor_result ^= 0
        if and_result >= xor_result:
            res += 1
    return res

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    # Count the number of arrays satisfying the condition
    print(f(0) % (10**9 + 7))
