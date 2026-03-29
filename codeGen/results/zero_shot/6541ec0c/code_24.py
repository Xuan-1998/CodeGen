import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        edges = []
        for _ in range(n-1):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u, v))

        # Your code goes here
        pass

if __name__ == "__main__":
    solve()
