from collections import defaultdict

def solve():
    T = int(input())
    dp = defaultdict(int)
    
    for _ in range(T):
        N = int(input())
        
        if N == 1:
            print(2)
        else:
            for i in range(N, 0, -1):
                if i % 2 == 0:
                    dp[i] = sum(dp[k] * (i-k+1) for k in range(min(i, 2), i))
                else:
                    dp[i] = dp[i-1]
            
            print(dp[N])

if __name__ == "__main__":
    solve()
