import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        k = len(str(n))  # initial number of digits
        result = (k + m) % (10**9 + 7)
        print(result)

if __name__ == "__main__":
    solve()
