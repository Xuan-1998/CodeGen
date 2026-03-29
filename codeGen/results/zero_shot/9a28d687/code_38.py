import sys
from functools import cmp_to_key

def sort_strings(costs, strings):
    # Sort the strings based on their lexicographical order
    sorted_strings = sorted(map(lambda s: s[::-1], strings), key=lambda x: x)
    
    total_cost = 0
    
    for i in range(len(sorted_strings) - 1):
        if sorted_strings[i] > sorted_strings[i + 1]:
            return -1
    
    # Calculate the minimum cost required to sort the strings
    for i, s in enumerate(strings):
        if s[::-1] != sorted_strings[i]:
            total_cost += costs[i]
    
    return total_cost

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    costs = list(map(int, sys.stdin.readline().split()))
    strings = [sys.stdin.readline().strip() for _ in range(n)]
    
    print(sort_strings(costs, strings))
