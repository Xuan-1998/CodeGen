import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        p = list(map(int, sys.stdin.readline().split()))
        if solve(p) == "YES":
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
