def solve():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    m = int(input())
    prime_factors = list(map(int, input().split()))
    
    # Calculate the maximum possible distribution index
    max_distribution_index = 0
    
    for i in range(n-1):
        for j in range(i+1, n):
            f_uv_sum = 0
            path_edges = []
            
            current_node = i
            while True:
                for edge in edges:
                    if edge[0] == current_node:
                        current_node = edge[1]
                        path_edges.append(edge)
                    elif edge[1] == current_node:
                        current_node = edge[0]
                        path_edges.append(edge)
                if j == current_node:
                    break
            for edge in path_edges:
                f_uv_sum += 1
            
            max_distribution_index += f_uv_sum
    
    print(max_distribution_index % (10**9 + 7))

if __name__ == "__main__":
    solve()
