def solve(n):
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]
    
    total_cost = 0
    
    # Sort the strings based on their lengths
    sorted_strings = sorted([(len(s), s) for s in strings])
    
    # Initialize a dictionary to store the cost of reversing each string
    cost_dict = {}
    
    for i, (_, s) in enumerate(sorted_strings):
        if s not in cost_dict:
            cost_dict[s] = costs[i]
    
    # Sort the strings based on their lengths and lexicographical order
    sorted_strings = sorted((s, cost_dict[s]) for s in set(strings))
    
    total_cost = 0
    prev_len = -1
    
    for s, c in sorted_strings:
        if len(s) < prev_len:
            total_cost += c
        else:
            break
        
        prev_len = len(s)
        
    return total_cost if prev_len >= 0 else -1

n = int(input())
print(solve(n))
