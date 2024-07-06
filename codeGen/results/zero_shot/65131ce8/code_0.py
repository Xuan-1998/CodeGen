def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    MOD = 998244353
    
    # Initialize the count of good vertices
    good_vertex_count = 0
    
    # To track the number of children each vertex has
    children = [0] * N
    
    # To track the parent of each vertex
    parent = [-1] * N
    
    # Start with the root
    current_vertex = 1
    for i in range(N):
        while d[i] > 0:
            children[i] += 1
            parent[current_vertex] = i
            d[i] -= 1
            current_vertex += 1
    
    # Function to determine if a vertex is good
    def is_good_vertex(v):
        current = v
        while parent[current] != -1:
            if parent[current] < v:
                return False
            current = parent[current]
        return True
    
    # Count good vertices
    for v in range(N):
        if is_good_vertex(v):
            good_vertex_count += 1
    
    # Output the result modulo 998244353
    print(good_vertex_count % MOD)

if __name__ == "__main__":
    main()

