import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        bits = [int(x) & (2 ** i - 1) for x in range(2 ** k)]
        count = 0
        for bit in set(bits):
            if bit != 0:
                count += 1
        print((2 ** k - 1) * (2 ** k - 2) // 2 % (10 ** 9 + 7))

if __name__ == "__main__":
    solve()
