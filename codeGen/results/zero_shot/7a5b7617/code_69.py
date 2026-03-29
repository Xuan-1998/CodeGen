import sys

def count_steady_tables():
    T = int(sys.stdin.readline())
    MOD = 10**9 + 7
    
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        total_sum = M * (N - 1)
        
        count = 0
        for row_sum in range(1, total_sum // N + 1):
            if (total_sum % N) >= row_sum and row_sum <= M:
                count += 1
        
        print(count % MOD)

count_steady_tables()
