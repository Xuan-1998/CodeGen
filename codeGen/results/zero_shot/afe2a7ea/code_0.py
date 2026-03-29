import sys

def solve():
    n = int(sys.stdin.readline())
    p = 0.5
    P = (1 - p) ** (n + 2) * p ** n * 2 ** (-n)
    print(int(P % 998244353))

if __name__ == "__main__":
    solve()
