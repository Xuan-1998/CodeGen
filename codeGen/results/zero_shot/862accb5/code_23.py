from collections import defaultdict

def find_cycle_util(v, visited, parent, adj):
    visited[v] = True
    for neighbor, weight in adj[v]:
        if not visited[neighbor]:
            if find_cycle_util(neighbor, visited, v, adj):
                return True
        elif neighbor != parent:
            return True
    return False

def find_cycle(n, adj):
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            if find_cycle_util(i, visited, -1, adj):
                return True
    return False

def find_max_edge_in_cycle(n, adj):
    # Assuming that a cycle exists
    max_edge_weight = 0
    for i in range(1, n + 1):
        for neighbor, weight in adj[i]:
            max_edge_weight = max(max_edge_weight, weight)
    return max_edge_weight

def main():
    n = int(input().strip())
    adj = defaultdict(list)
    total_inconvenience = 0
    
    for _ in range(n):
        u, v, l = map(int, input().strip().split())
        adj[u].append((v, l))
        adj[v].append((u, l))
        total_inconvenience += l

    max_edge_weight = find_max_edge_in_cycle(n, adj)
    min_inconvenience = total_inconvenience - max_edge_weight
    print(min_inconvenience)

if __name__ == "__main__":
    main()
