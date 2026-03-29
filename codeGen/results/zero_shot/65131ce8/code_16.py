def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    MOD = 998244353
    
    # To count the number of good vertices
    good_vertex_count = 0
    
    # We need to check each vertex if it can be a good vertex
    for i in range(N):
        if d[i] == 0:
            good_vertex_count += 1
    
    # The number of valid configurations is given by the number of good vertices
    result = good_vertex_count % MOD
    
    print(result)

if __name__ == "__main__":
    main()

