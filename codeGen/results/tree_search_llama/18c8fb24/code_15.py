import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, x, k = map(int, sys.stdin.readline().split())
        n = 0
        while True:
            if (n * k + x) <= x:
                print("YES")
                break
            n += 1
        print("NO")

if __name__ == "__main__":
    solve()
