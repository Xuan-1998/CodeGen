import sys

def infinite_zoo_queries():
    q = int(sys.stdin.readline())
    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        if v == u & v:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    infinite_zoo_queries()
