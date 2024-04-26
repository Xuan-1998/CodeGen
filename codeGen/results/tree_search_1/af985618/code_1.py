MOD = 998244353

def main():
    n = int(input())
    A = [input().split() for _ in range(n)]
    
    # Separate and sort positive elements
    positives = sorted([int(x) for op, x in A if op == '+'])
    num_positives = len(positives)
    
    # Precompute factorials for combinations
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    # Precompute inverse of factorial for combinations
    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    # Function to compute nCr modulo MOD
    def nCr(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] * inv_fact[n - r] % MOD
    
    # Dynamic programming to calculate the contribution of each positive element
    answer = 0
    for i, x in enumerate(positives):
        # Count the number of negative elements before the current positive element
        neg_count = sum(1 for op, _ in A if op == '-' and A.index([op, _]) < A.index(['+', str(x)]))
        # Calculate the contribution of the current positive element
        for k in range(neg_count + 1):
            answer += x * nCr(neg_count, k) * nCr(num_positives - 1, num_positives - 1 - k) % MOD
            answer %= MOD
    
    print(answer)

if __name__ == "__main__":
    main()
