import sys

def solve():
    n = int(sys.stdin.readline())
    mod = 998244353
    ans = pow(2, n-1, mod)
    print(ans)

if __name__ == "__main__":
    solve()
