import sys

def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().strip().split())
        if m == 0:
            print(n % (10**9 + 7))
        else:
            while m > 0:
                n = sum(int(d) + 1 for d in str(n)) * (n == 0)
                m -= 1
            print(len(str(n)) % (10**9 + 7))

if __name__ == "__main__":
    main()
