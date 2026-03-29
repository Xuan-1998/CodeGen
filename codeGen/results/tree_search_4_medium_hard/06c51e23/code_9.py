import sys

def solve():
    n, t = map(int, input().split())
    dp = [0] * (n + 1)
    memo = {0: 0}
    
    for i in range(1, n + 1):
        round_up = dp[i - 1] if not memo.get(i - 1) else memo[i - 1]
        round_down = dp[i - 1] if not memo.get(i - 1) or int(frac[i - 1]) < 4 else 0
        
        max_grade = max(round_up, round_down)
        dp[i] = max_grade
        memo[i] = max_grade
    
    return str(dp[-1])

if __name__ == "__main__":
    print(solve())
