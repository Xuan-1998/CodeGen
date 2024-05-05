import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        if n > 1:
            res = (m + 1) ** (n - 1)
        else:
            res = 1
        print(res % 1000000000)

if __name__ == "__main__":
    solve()
