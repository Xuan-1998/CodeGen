import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        M, X = map(int, sys.stdin.readline().split())
        winners = []
        for i in range(1, X+1):
            winner = ((i-1) * (M-1)) % i
            winners.append(str(winner+1))
        print(' '.join(winners))

if __name__ == "__main__":
    solve()
