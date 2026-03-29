import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        res_and, res_xor = 0, 0
        for i in range(n):
            x = int(input())
            and_mask = (1 << k) - 1
            xor_mask = and_mask ^ ((1 << k + 1) - 1)
            if (x & and_mask) >= xor_mask:
                res_and += 1
            if (x & xor_mask) == xor_mask:
                res_xor += 1
        print((res_and * res_xor) % (10**9 + 7))

if __name__ == "__main__":
    solve()
