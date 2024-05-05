import sys

def min_total_cost(strings):
    # Sort the strings by their lengths and costs
    sorted_strings = sorted((len(s), c, s) for s, c in zip(strings, [int(x) for x in input().split()]))
    
    total_cost = 0
    prev_len = None
    
    for _, cost, s in sorted_strings:
        if len(s) < prev_len:
            # If the string is shorter than the previous one, we need to reverse it
            total_cost += cost
        elif len(s) == prev_len:
            # If the strings have the same length, we can sort them alphabetically
            pass
        else:
            # If the string is longer than the previous one, we don't need to do anything
            pass
        
        prev_len = len(s)
    
    return total_cost if prev_len is not None else -1

n = int(input())
strings = [input() for _ in range(n)]
print(min_total_cost(strings))
