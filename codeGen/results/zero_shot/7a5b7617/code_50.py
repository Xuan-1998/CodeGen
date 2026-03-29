import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        count = 0
        for row in range(N):
            for col in range(M+1):
                if row < N-1 or col <= M:
                    count += 1
        print(count % (10**9 + 7))

if __name__ == "__main__":
    solve()
