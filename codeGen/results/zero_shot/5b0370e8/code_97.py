import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        total_and, total_xor = 0, 0
        for _ in range(n):
            num = int(input())
            and_bit = num & ((1 << (k - 1)) - 1)
            xor_bit = num ^ ((1 << (k - 1)) - 1)
            if and_bit >= xor_bit:
                total_and += 1
        print(total_and % (10**9 + 7))

if __name__ == "__main__":
    solve()
