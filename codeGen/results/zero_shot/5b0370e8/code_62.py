import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        res_and = 0
        res_xor = 0
        for _ in range(n):
            num = int(sys.stdin.readline())
            and_mask = (1 << k) - 1
            if num & and_mask:
                res_and += 1
            res_xor ^= num
        print((res_and >= res_xor).count(True) % (10**9 + 7))

if __name__ == "__main__":
    solve()
