from collections import defaultdict

def solve():
    t = int(input())
    
    memo = defaultdict(int)
    memo[(0, 0)] = 1
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(max(m - i * (i - 1), 0), m + 1):
                if i > 1:
                    dp[i][j] += sum(dp[i - 1].values()) % 1000000000
                else:
                    dp[i][j] = (m - j) % 1000000000 + 1
                
        print((dp[-1][-1]) % 1000000000)

if __name__ == "__main__":
    solve()
