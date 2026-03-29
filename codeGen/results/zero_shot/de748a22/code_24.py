import sys

def process_query(signs, l, r):
    total_signs = 0
    ones_count = 0
    zeros_count = 0
    
    for i in range(l-1):
        if signs[i] == "+":
            ones_count += 1
        else:
            zeros_count += 1
        
        total_signs += signs[i]
    
    new_total_signs = total_signs + (r-l+2)
    
    if new_total_signs > 0:
        return min(ones_count, zeros_count)
    else:
        return max(ones_count, zeros_count)

n, q = map(int, sys.stdin.readline().split())
signs = list(sys.stdin.readline())

for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())
    print(process_query(signs, l, r))
