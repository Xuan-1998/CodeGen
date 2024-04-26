import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, x, k = map(int, sys.stdin.readline().split())
        if (x % k) > (N % k):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
