import sys
from collections import defaultdict

def main():
    T = int(input())  # Read test cases from stdin
    
    for _ in range(T):
        n = int(input())  # Number of vertices
        
        parent = defaultdict(int)  # Parent pointers for each vertex
        ranges = {}  # Ranges for each vertex
        
        for i in range(1, n+1):  # Read parent and range information from stdin
            if i == 1:
                parent[1] = None
            else:
                parent[i] = int(input())
            l, r = map(int, input().split())  # Read range [l, r]
            ranges[i] = (l, r)
        
        operations = 0
        
        def dfs(node):
            nonlocal operations
            
            if node not in ranges:  # Base case: leaf node
                return 0
            
            l, r = ranges[node]
            diff = max(l - 1, min(r + 1) - r)  # Calculate the range adjustment needed
            operations += diff  # Update the total number of operations
            
            if parent[node]:  # Recursively update ancestors
                dfs(parent[node])
        
        for i in range(2, n+1):
            dfs(i)
        
        print(operations)  # Print the minimum number of operations

if __name__ == "__main__":
    main()
