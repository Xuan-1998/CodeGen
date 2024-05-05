import math
import sys

def solve():
    n = int(sys.stdin.readline().split()[0])
    t = int(sys.stdin.readline())
    
    dp = [1]
    max_grade = 0
    
    for i in range(1, n):
        new_dp = []
        for j in range(i+1):
            round_up = math.floor(int('9' * (i-j)) / 10**(i-j) + 0.5)
            round_down = int('1' * (i-j))
            
            if j == i:
                grade = min(round_up, round_down)
            else:
                new_dp.append(min(grade + round_up, grade + round_down))
        
        dp = new_dp
        max_grade = max(dp[-1], max_grade)
    
    for _ in range(t-1):
        new_dp = [0]
        for i in range(len(dp) - 1, 0, -1):
            if dp[i] >= dp[0]:
                new_dp.append(min(new_dp[-1] + dp[i], dp[0]))
            else:
                new_dp.append(dp[0])
        
        dp = new_dp
        max_grade = max(dp)
    
    print(int(max_grade))

solve()
