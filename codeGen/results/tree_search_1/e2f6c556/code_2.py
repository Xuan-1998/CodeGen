from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def dfs(node, adj, visited, rec_stack, stack):
    visited[node] = True
    rec_stack[node] = True
    
    for neighbor in adj[node]:
        if not visited[neighbor]:
            if dfs(neighbor, adj, visited, rec_stack, stack):
                return True
        elif rec_stack[neighbor]:
            return True
    
    rec_stack[node] = False
    stack.append(node)
    return False

def longest_path_length(adj, n):
    visited = [False] * n
    rec_stack = [False] * n
    stack = []
    
    for node in range(n):
        if not visited[node]:
            if dfs(node, adj, visited, rec_stack, stack):
                return -1
    
    order = stack[::-1]
    longest_path = [0] * n
    
    for node in order:
        for neighbor in adj[node]:
            longest_path[neighbor] = max(longest_path[neighbor], longest_path[node] + 1)
    
    return max(longest_path) + 1

def main():
    input_data = sys.stdin.read().splitlines()
    iterator = iter(input_data)
    while True:
        try:
            n = int(next(iterator))
            adj = defaultdict(list)
            for i in range(n):
                line = list(map(int, next(iterator).split()))
                k = line[0]
                for j in range(1, k + 1):
                    adj[line[j] - 1].append(i)
            
            result = longest_path_length(adj, n)
            print(result)
        except StopIteration:
            break

if __name__ == "__main__":
    main()
