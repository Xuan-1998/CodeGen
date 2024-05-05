import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        and_result = 2**k - 1
        xor_result = 0
        for _ in range(n):
            num = int(sys.stdin.readline())
            and_result &= num
            xor_result ^= num
        count = (and_result >= xor_result) + 1
        print(count % (10**9 + 7))

if __name__ == "__main__":
    solve()
