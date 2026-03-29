import sys

def solve():
    n, q, c = map(int, sys.stdin.readline().split())
    stars = []
    for _ in range(n):
        x, y, s = map(int, sys.stdin.readline().split())
        stars.append((s, x, y, 0))

    memo = {}

    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        result = 0

        if (x1, y1, x2, y2) not in memo:
            for s, x, y in stars:
                if x1 <= x <= x2 and y1 <= y <= y2:
                    t %= c
                    while t > 0:
                        result += s
                        t -= 1

        print(result)

if __name__ == "__main__":
    solve()
