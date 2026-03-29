import sys

def solve(n, k):
    MOD = 1000000007
    total_arrays = pow(2, n, MOD)
    and_result = 0
    for _ in range(k-1):
        and_result <<= 1
    
    count_and_geq_xor = 0
    for mask in range(1 << k):
        if (and_result & mask) >= mask:
            count_and_geq_xor += 1
    
    return (total_arrays - count_and_geq_xor) % MOD

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
