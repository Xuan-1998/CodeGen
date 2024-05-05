import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        total_and, total_xor = 0, 0
        for _ in range(n):
            num = int(sys.stdin.readline())
            and_val = num & ((1 << k) - 1)
            xor_val = num ^ (num >> 1)
            total_and |= and_val
            total_xor ^= xor_val
        if total_xor == 0:
            print(1)
        else:
            and_bits = bin(total_and)[2:]
            xor_bits = bin(total_xor)[2:]
            common_prefix_len = 0
            for i in range(min(len(and_bits), len(xor_bits))):
                if and_bits[i] == xor_bits[i]:
                    common_prefix_len += 1
                else:
                    break
            print((1 << (k - common_prefix_len)) % (10 ** 9 + 7))

if __name__ == "__main__":
    solve()
