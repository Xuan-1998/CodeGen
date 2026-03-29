import sys

def and_xor_count():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        count = 0
        xor_sum = 0
        for _ in range(n):
            num = int(input())
            xor_sum ^= num
            if xor_sum & 1:
                count += 1
        print(count % (10**9 + 7))

and_xor_count()
