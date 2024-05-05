import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        result = str(n)
        for _ in range(m):
            new_result = ''
            for d in result:
                new_result += str((int(d) + 1) % 10)
            result = new_result
        print(len(result) % (10**9 + 7))

solve()
