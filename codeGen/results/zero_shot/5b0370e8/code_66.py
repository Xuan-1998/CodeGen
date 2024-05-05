import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        ans = 0
        for _ in range(n):
            x = int(sys.stdin.readline())
            if x & (2**k-1) >= x ^ (2**k-1):
                ans += 1
        print(ans % (10**9+7))

if __name__ == "__main__":
    solve()
