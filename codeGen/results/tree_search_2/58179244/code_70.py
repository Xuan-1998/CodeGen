import sys
from collections import defaultdict

def solve():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    
    memo = {i: {} for i in range(n+1)}
    
    min_recolor_count = float('inf')
    optimal_solution = None
    
    for i in range(1, n):
        prev_color = s[i-1]
        curr_color = s[i]
        
        if prev_color == curr_color:
            recolor_count = 0
            for j in range(i+1, n):
                if s[j] == prev_color:
                    recolor_count += 1
                else:
                    break
            
            memo[i][curr_color] = (recolor_count + int(curr_color != prev_color), curr_color)
        else:
            memo[i][curr_color] = (int(curr_color != prev_color), curr_color)
    
    for i in range(n-1, -1, -1):
        if memo[i]:
            min_recolor_count = min(min_recolor_count, memo[i][s[i]][0])
            optimal_solution = s[:i+1] + memo[i][s[i]][1]
    
    print(min_recolor_count)
    print(optimal_solution)

solve()
