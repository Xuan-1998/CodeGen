import sys

def num_ways(n_rows, n_cols):
    if (n_rows == N) or (n_rows >= M):
        return 1

    cache = {}
    
    def dp(n_rows, n_cols):
        key = (n_rows, n_cols)
        
        if key in cache:
            return cache[key]
        
        res = 0
        for i in range(min(n_cols, M)):
            res += dp(n_rows + 1, min(i + 1, M))
        cache[key] = res % 1000000000
        return res % 1000000000

    N, M = map(int, input().split())
    print(dp(0, n_cols))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(num_ways(N, M))
