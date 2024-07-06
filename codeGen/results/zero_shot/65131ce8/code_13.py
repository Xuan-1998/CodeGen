python
MOD = 998244353

def count_good_vertices(N, d):
    # Calculate factorials and inverse factorials for combinatorial calculations
    fact = [1] * (N + 1)
    inv_fact = [1] * (N + 1)
    for i in range(2, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

    # Function to calculate nCr % MOD
    def comb(n, r):
        if r > n or r < 0:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

    # Count the number of good vertices
    good_vertex_count = 0
    for i in range(1, N + 1):
        if d[i - 1] == 0:
            good_vertex_count += 1

    # Calculate the number of good trees
    good_trees_count = 1
    for i in range(1, N):
        good_trees_count = good_trees_count * comb(i + d[i], d[i]) % MOD

    # Sum of good vertices for all good trees
    result = good_vertex_count * good_trees_count % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    d = list(map(int, data[1:]))
    print(count_good_vertices(N, d))

