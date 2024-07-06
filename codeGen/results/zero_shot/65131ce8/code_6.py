def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    MOD = 998244353
    
    # Check constraints
    assert 2 <= N <= 500
    assert len(d) == N
    assert sum(d) == N - 1
    assert all(0 <= di <= N - 1 for di in d)
    assert d[0] >= 1
    
    # Since d[0] >= 1, vertex 1 is always a good vertex
    good_vertex_count = 1
    
    # To find the number of good vertices
    for i in range(1, N):
        if d[i] == 0:
            good_vertex_count += 1
    
    # The result is the number of good vertices modulo 998244353
    result = good_vertex_count % MOD
    
    print(result)

if __name__ == "__main__":
    main()

