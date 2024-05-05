import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, C = map(int, sys.stdin.readline().split())
        U = list(map(int, sys.stdin.readline().split()))
        L = list(map(int, sys.stdin.readline().split()))
        
        # Initialize the count of X-sequences
        seq_count = [0] * (C + 1)
        
        # Count the number of X-sequences for each radius
        for r in range(1, C + 1):
            seq_count[r] += sum(1 for u in U if u <= r) * sum(1 for l in L if l >= r)
        
        # Print the count of X-sequences modulo 10^9+7
        print(*[seq_count[i] % (10**9 + 7) for i in range(C + 1)], sep=' ')

if __name__ == '__main__':
    solve()
