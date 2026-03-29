import sys

def solve():
    n, t = map(int, input().split())
    fractional_part = [int(x) for x in input().split('.')][1]
    
    dp = [0] * (n + 1)
    available_time = [t] * (n + 1)

    for i in range(1, n + 1):
        round_up = max(dp[i - 1], fractional_part[i - 1])
        round_down = max(dp[i - 1], fractional_part[i - 1] - 1)
        
        available_time[i] = min(available_time[i - 1], round_up)
        dp[i] = max(dp[i - 1], round_up, round_down)

    print(max(0, dp[-1]))

if __name__ == "__main__":
    solve()
