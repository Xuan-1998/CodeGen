import sys

def count_ways(M):
    MOD = 10**9 + 7
    n = len(M)
    count = 0
    for _ in range(2**n):  # iterate through each possible array in V
        v = [0] * n
        for i in range(n):
            if (_ & (1 << i)):  # check if the ith element is included in the current array
                v[i] = M[i]
        if sorted(v) == M:  # merge V into a sorted array and check if it's equal to M
            count += 1
    return pow(count, MOD, MOD)

n = int(input())
M = list(map(int, input().split()))
print(count_ways(M))
