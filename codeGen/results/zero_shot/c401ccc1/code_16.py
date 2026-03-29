import sys
input = sys.stdin.readline

def main():
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        if u & v == v:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
