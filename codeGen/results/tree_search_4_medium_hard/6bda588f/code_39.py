import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        dp = {(i, prev_F): float('inf') for i in range(n + 1) for prev_F in range(2 * sys.maxsize + 1)}
        dp[(0, 0)] = 0
        for i in range(1, n + 1):
            min_val = float('inf')
            for x_i in range(s + 1):
                y_i = a[i - 1] - x_i
                if (x_i - s) * (y_i - s) >= 0:
                    new_F = dp[(i - 1, prev_F)] + a[i - 1] * min(x_i, s) + y_i * max(x_i, s)
                    if new_F < min_val:
                        min_val = new_F
            dp[(i, prev_F)] = min_val
        print(min(dp.values()))

if __name__ == "__main__":
    solve()
