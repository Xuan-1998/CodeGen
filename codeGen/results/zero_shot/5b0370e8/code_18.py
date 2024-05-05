import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        and_count = [0] * (k + 1)
        xor_count = [0] * (k + 1)
        for num in map(int, sys.stdin.readline().split()):
            for i in range(k + 1):
                bit = (num >> i) & 1
                if bit:
                    and_count[i] += 1
                    xor_count[i] ^= 1
                else:
                    and_count[i] -= 1
        count = 0
        for i in range(k + 1):
            if and_count[i] % 2 == 0:
                count += (xor_count[i] + 1) // 2
        print(count % (10**9 + 7))

if __name__ == "__main__":
    solve()
