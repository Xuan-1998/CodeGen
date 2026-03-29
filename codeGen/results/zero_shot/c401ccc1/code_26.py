import sys

def infinite_zoo_queries():
    q = int(sys.stdin.readline())
    vertices = set()
    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        w = u & v
        if w not in vertices and (u & w == w and v & w == w):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    infinite_zoo_queries()
