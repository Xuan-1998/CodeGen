import sys

def solve():
    t = int(input())
    mod = 10**9 + 7
    
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        
        dp = [[0] * (k+1) for _ in range(n+1)]
        count = 1
        
        for x in arr:
            if dp[x][k]:
                for y in range(x+1, n+1):
                    dp[y][k] = True
            else:
                dp[x][k] = False
            
            if dp[x][k]:
                count += 1
        
        print(count % mod)

if __name__ == "__main__":
    solve()
