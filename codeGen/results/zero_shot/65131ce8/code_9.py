python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    MOD = 998244353
    
    # Calculate the factorial and factorial inverse modulo MOD
    fact = [1] * (N + 1)
    inv_fact = [1] * (N + 1)
    
    for i in range(2, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    inv_fact[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    # Function to calculate nCk % MOD
    def comb(n, k):
        if k > n or k < 0:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
    
    # Calculate the number of good vertices
    good_vertices_count = 0
    
    for i in range(N):
        if d[i] == 0:
            continue
        
        # Count the number of ways to arrange the children of vertex i
        children_count = d[i]
        remaining_vertices = N - 1 - children_count
        
        if remaining_vertices < 0:
            continue
        
        good_vertices_count += comb(remaining_vertices, children_count)
        good_vertices_count %= MOD
    
    print(good_vertices_count)

if __name__ == "__main__":
    main()

