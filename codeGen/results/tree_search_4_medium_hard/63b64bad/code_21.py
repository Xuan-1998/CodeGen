import sys
from collections import defaultdict

def simulate_sequence(a):
    dp = defaultdict(lambda: [-1 for _ in range(len(a))])
    y_max = 0
    
    for x in range(2, len(a) + 1):
        if a[x-1] <= 0 or a[x-1] > len(a):
            continue
        
        for i in range(x):
            new_x = i + a[i]
            new_y = y_max + a[i]
            
            if (new_x, new_y) not in dp:
                dp[(new_x, new_y)] = [new_x, new_y]
                
            if x <= 0 or x > len(a):
                return -1
                
        y_max = max(y_max, dp[(x-1, y_max)][1])
        
    return y_max

n = int(input())
a = list(map(int, input().split()))
print(simulate_sequence(a))
