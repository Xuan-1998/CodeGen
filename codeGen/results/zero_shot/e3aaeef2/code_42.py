import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        length = len(str(n)) + m
        print(length % (10**9 + 7))

if __name__ == "__main__":
    main()
