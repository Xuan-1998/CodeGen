import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, x, k = map(int, sys.stdin.readline().split())
        A = [[1, 0], [0, -1]]
        v = [x, 0]
        for _ in range(N // k):
            v = [[A @ v][0]]
        if v[0] > N:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
