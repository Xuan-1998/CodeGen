import sys

def solve():
    T = int(input())
    memo = {}
    
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        
        dp = [[0] * (C + 1) for _ in range(N + 1)]
        
        def dfs(i, j):
            if (i, j) not in memo:
                if i == 0 and j == 0:
                    result = 1
                elif i > 0 and j > 0:
                    result = sum(dfs(k, j) for k in range(i)) * sum(dfs(i, l) for l in range(j))
                else:
                    result = (i + 1) if i > 0 else (j + 1)
                memo[(i, j)] = result
            return memo[(i, j)]
        
        total = 0
        for i in range(N + 1):
            for j in range(M + 1):
                total += dfs(i, j) % (10**9 + 7)
        print(total)

if __name__ == "__main__":
    solve()
