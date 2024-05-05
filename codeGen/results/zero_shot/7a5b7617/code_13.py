import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        tables = set()
        for row in range(N):
            sums = []
            for col in range(M):
                total = 0
                while True:
                    num = min(M - sum(sums), int(1e9) // (N - row))
                    total += num
                    if total > M or len(sums) == N - row:
                        break
                    sums.append(num)
            tables.add(tuple(sums))
        print(len(tables) % 1000000000)

if __name__ == "__main__":
    solve()
