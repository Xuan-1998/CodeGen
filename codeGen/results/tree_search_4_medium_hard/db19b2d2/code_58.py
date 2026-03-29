import sys

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    t = [0] * (n + 1)
    for i in range(1, m + 1):
        t[i] = min(t[i - 1], 1 + s[i - 1])

    ans = 1 - sum([t[i] / n for i in range(h + 1)]) if h > 0 else 0
    print(ans)

if __name__ == "__main__":
    solve()
