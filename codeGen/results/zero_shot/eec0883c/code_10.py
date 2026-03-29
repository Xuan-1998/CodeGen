import sys

def main():
    n = int(sys.stdin.readline())
    w = [int(x) for x in sys.stdin.readline().split()]
    c = [int(x) for x in (sys.stdin.readline() for _ in range(n-1))]

    print(max_gasoline(n, w, c))

if __name__ == "__main__":
    main()
