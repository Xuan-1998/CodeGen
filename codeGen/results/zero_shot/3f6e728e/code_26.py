import sys

def solve():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        N, M, C = map(int, sys.stdin.readline().split())
        U = list(map(int, sys.stdin.readline().split()))
        L = list(map(int, sys.stdin.readline().split()))
        
        # Calculate the number of X-sequences
        x_sequences = 1
        for i in range(C):
            if i < N:
                x_sequences *= (i + 1)
            if i < M:
                x_sequences *= (C - i)
        
        print(x_sequences % (10**9 + 7))

if __name__ == "__main__":
    solve()
