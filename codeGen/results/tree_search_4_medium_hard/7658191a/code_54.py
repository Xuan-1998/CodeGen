import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        scores = list(map(int, input().split()))
        
        dp = [0] * (k + 1)
        prev_max = 0
        for i in range(k + 1):
            if i <= z:
                dp[i] = max(dp[i], prev_max + scores[i])
            else:
                dp[i] = max(dp[i], dp[i - 1] + scores[i])
            prev_max = dp[i]
        
        print(max(dp))

if __name__ == "__main__":
    solve()
