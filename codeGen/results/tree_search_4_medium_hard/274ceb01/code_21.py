import sys

def solve():
    n = int(input())
    marks_above_water_level = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        total_marks_above_water_level_on_prev_days = sum(marks_above_water_level[:i])
        dp[i] = total_marks_above_water_level_on_prev_days * (i - 1) - total_marks_above_water_level_on_prev_days
        
    print(min(dp))

if __name__ == "__main__":
    solve()
