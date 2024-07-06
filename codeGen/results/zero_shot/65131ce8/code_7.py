MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().strip().split()))
    
    N = data[0]
    d = data[1:]
    
    # Calculate the number of good vertices
    good_vertices_count = 0
    
    # We need to find the number of good vertices in all good trees
    # For a vertex to be good, it should be the smallest in its subtree
    # This is true if and only if it has no ancestors with a smaller number
    
    # The root (vertex 1) is always a good vertex
    good_vertices_count += 1
    
    # For each vertex, if it has an out-degree greater than 0, it can be a good vertex
    for i in range(1, N):
        if d[i] > 0:
            good_vertices_count += 1
    
    # Output the result modulo 998244353
    print(good_vertices_count % MOD)

if __name__ == "__main__":
    main()

