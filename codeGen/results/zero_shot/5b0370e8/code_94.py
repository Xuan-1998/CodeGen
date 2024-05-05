import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        and_result = 2 ** (k - 1) - 1
        xor_result = sum((i >> j) & 1 for i in range(2**k)) % (10**9 + 7)
        count = ((and_result ^ xor_result) >> k) & 1
        print(count)

if __name__ == "__main__":
    solve()
