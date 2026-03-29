import sys

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[{} for _ in range(10**9+1)] for _ in range(n+1)]
    
    # Initialization
    for i in range(n):
        dp[i][0][0] = 1
    
    for i in range(n-1):
        u, v = map(int, input().split())
        xor_val = a[u] ^ a[v]
        for j in range(1, k+1):
            if (a[u] ^ xor_val) % 2 == 0 and dp[u][j-1].get(xor_val, 0):
                dp[i+1][j][xor_val] = 1
            if (a[v] ^ xor_val) % 2 == 0 and dp[v][j-1].get(xor_val, 0):
                dp[i+1][j][xor_val] = 1
    
    for j in range(1, k+1):
        if any(dp[n-1][j-1].get(xor_val, 0) for xor_val in set(a)):
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    solve()
