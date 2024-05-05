import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        print(min((a[i-1] - j) * (a[i]-j) for i, j in enumerate(a)))

if __name__ == "__main__":
    solve()
