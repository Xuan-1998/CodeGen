import sys

def dp_function(current_time):
    if current_time > k[-1]:
        return 0
    
    if (current_time, 0) in dp:
        return dp[(current_time, 0)]
    
    min_mana = float('inf')
    for i, (ki, hi) in enumerate(zip(k, h)):
        if ki == current_time:
            for damage in range(hi, sys.maxsize):
                min_mana = min(min_mana, dp_function(k[i+1]) + damage)
    
    dp[(current_time, 0)] = min_mana
    return min_mana

n = int(input())
k = list(map(int, input().split()))
h = list(map(int, input().split()))
print(dp_function(1))
