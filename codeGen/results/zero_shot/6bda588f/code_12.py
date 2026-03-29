import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        ans = 0
        for i in range(n - 1):
            y_i = max(s // 2, a[i] - (a[i + 1] - s) // 2)
            x_i = a[i] - y_i
            ans += x_i * y_i
        print(ans)

if __name__ == "__main__":
    solve()
