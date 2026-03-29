import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        count = pow(2, n-k, 10**9+7)
        print(count)

if __name__ == "__main__":
    solve()
