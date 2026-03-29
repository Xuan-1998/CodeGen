import sys
from itertools import product

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        bits = [int(x, 2) for x in input().split()]
        and_count = 0
        xor_count = 0
        for a in product('0', '1') * n:
            a_int = int(''.join(a), 2)
            and_result = sum((a_int >> i) & bits[i] for i in range(n))
            xor_result = sum((a_int ^ bits[i]) for i in range(n))
            if and_result >= xor_result:
                and_count += 1
        print((and_count % (10**9 + 7)))

if __name__ == '__main__':
    solve()
