import math

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        count = 0
        for _ in range(n):
            x = int(input())
            if (x & ((1 << k) - 1)) == 0:
                count += 1
        print((count + 7) % (10**9 + 7))

solve()
