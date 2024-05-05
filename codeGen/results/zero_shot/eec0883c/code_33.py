import sys

def solve():
    n = int(sys.stdin.readline())
    w = [int(x) for x in sys.stdin.readline().split()]
    roads = []
    for _ in range(n-1):
        u, v, c = map(int, sys.stdin.readline().split())
        roads.append((u, v, c))

    # Implement the solution here...

if __name__ == '__main__':
    solve()
