python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    MOD = 998244353
    
    # Step 1: Calculate the factorials and inverse factorials
    fact = [1] * (N + 1)
    inv_fact = [1] * (N + 1)
    
    for i in range(2, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    inv_fact[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    # Step 2: Calculate the number of good vertices
    good_vertices_count = 0
    for i in range(1, N + 1):
        if d[i - 1] == 0:
            continue
        good_vertices_count += fact[N - 1] * inv_fact[d[i - 1]] % MOD * inv_fact[N - 1 - d[i - 1]] % MOD
        good_vertices_count %= MOD
    
    print(good_vertices_count)

if __name__ == "__main__":
    main()

