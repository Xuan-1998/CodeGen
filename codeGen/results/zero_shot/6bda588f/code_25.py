import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        min_f = float('inf')
        for x in range(s + 1):
            y = a[0] - x
            if y <= s:
                f = x * (a[0] - x)
                for i in range(1, n):
                    x = min(x, a[i] // 2) if x > 0 else 0
                    y = min(y, a[i] - x)
                    f *= x * (y // x)
                min_f = min(min_f, f)
        print(min_f)

if __name__ == '__main__':
    solve()
