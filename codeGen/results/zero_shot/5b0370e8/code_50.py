import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_count = 1
        xor_count = 0
        for _ in range(n):
            num = int(input())
            and_bitwise_xor = (and_count & num) + (xor_count ^ num)
            if and_bitwise_xor >= num:
                and_count += and_count
            else:
                xor_count += xor_count
            print(and_count % (10**9 + 7))

solve()
