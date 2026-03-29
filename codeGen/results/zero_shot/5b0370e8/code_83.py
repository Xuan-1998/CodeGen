import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        count = 0
        for _ in range(n):
            x = int(sys.stdin.readline(), 2)
            if x & (x ^ ((1 << k) - 1)):
                count += 1
        print(count % (10**9 + 7))

if __name__ == "__main__":
    solve()
