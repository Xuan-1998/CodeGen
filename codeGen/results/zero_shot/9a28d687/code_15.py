import sys
from collections import defaultdict

def solve():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]

    # Create a Trie data structure to store all the strings
    trie = defaultdict(list)
    for string in strings:
        node = trie
        for char in string:
            if char not in node:  # If this character is not present, create it
                node[char] = []
            node = node[char]
        node.append(string)  # Store the string at the last node

    min_cost = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            if strings[i] > strings[j]:  # If string i is greater than string j
                cost_to_sort = costs[i] + costs[j]
                if cost_to_sort < min_cost:
                    min_cost = cost_to_sort

    if min_cost == float('inf'):
        return -1
    else:
        return min_cost

print(solve())
