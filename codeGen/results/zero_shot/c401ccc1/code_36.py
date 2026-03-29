import sys

def infinite_zoo(q):
    for _ in range(q):
        u, v = map(int, input().split())
        if not (v & u):  # no path exists
            print("NO")
        else:
            while True:
                if v == u:  # found a path
                    print("YES")
                    break
                if v & u != v:  # no path exists
                    print("NO")
                    break
                u, v = v, v & u

if __name__ == "__main__":
    q = int(input())
    infinite_zoo(q)
