import sys

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    max_sum = 0
    prev_xor = 0
    for i in range(1, n):
        xor = a[i-1] ^ a[i]
        prev_xor += xor
        max_sum = max(max_sum, prev_xor)

    # Handle the operation of adding X to at most one subsequence
    max_sum += x

    print(max_sum)
