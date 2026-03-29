import sys

def mergeable(p):
    n = len(p) // 2
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    def dfs(i, j, c):
        if i >= n and j >= n:
            return True
        
        if not dp[i][j]:
            if p[i] < p[j]:
                dp[i][j] = dfs(i + 1, j, False)
            elif p[i] > p[j]:
                dp[i][j] = dfs(i, j + 1, False)
            else:
                dp[i][j] = c
        
        return dp[i][j]
    
    for i in range(n):
        if not dfs(i, i, True):
            return "NO"
    
    return "YES"

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        p = list(map(int, input().split()))
        
        if len(p) != 2 * n or min(p) < 0 or max(p) > 2 * n - 1:
            print("NO")
            continue
        
        print(mergeable(p))

if __name__ == "__main__":
    main()
