import sys

def dp(tail_length, number_of_spines):
    if (tail_length, number_of_spines) in memo:
        return memo[(tail_length, number_of_spines)]
    
    max_beauty = 0
    
    for i in range(m - 1, -1, -1):
        u, v = edges[i]
        
        if u not in tail or v == tail[-1]:
            continue
        
        new_tail_length = len(tail) + 1
        new_spines = number_of_spines + 1
        
        max_beauty = max(max_beauty, dp(new_tail_length, new_spines))
    
    memo[(tail_length, number_of_spines)] = tail_length * number_of_spines + max_beauty
    return memo[(tail_length, number_of_spines)]

n, m = map(int, sys.stdin.readline().split())
memo = {}
edges = [map(int, sys.stdin.readline().split()) for _ in range(m)]

max_beauty = 0

for i in range(n):
    if i not in tail:
        continue
    
    max_beauty = max(max_beauty, dp(i + 1, 1))
    
print(max_beauty)
