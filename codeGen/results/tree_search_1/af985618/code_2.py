MOD = 998244353

def modinv(x, m):
    return pow(x, m - 2, m)

def solve(n, A):
    # Precompute factorials and their modular inverses for binomial coefficients
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % MOD
        inv_fact[i] = modinv(fact[i], MOD)
    
    def binom(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] * inv_fact[n - k] % MOD
    
    answer = 0
    for i in range(n):
        if A[i][0] == '+':
            x = int(A[i][1])
            # Count the number of ways to form subsequences before and after the current element
            ways_before = ways_after = 0
            balance = 0  # Balance of + and - before the current element
            for j in range(i):
                if A[j][0] == '+':
                    balance += 1
                else:
                    balance -= 1
                    if balance >= 0:
                        ways_before += binom(i - 1, balance)
                        ways_before %= MOD
            balance = 0  # Balance of + and - after the current element
            for j in range(i + 1, n):
                if A[j][0] == '+':
                    balance += 1
                else:
                    balance -= 1
            for k in range(balance + 1):
                ways_after += binom(n - i - 1, k)
                ways_after %= MOD
            # Multiply the ways before and after and the value of x
            answer += x * ways_before * ways_after % MOD
            answer %= MOD
    return answer

# Read input
n = int(input().strip())
A = [input().strip().split() for _ in range(n)]

# Solve the problem and print the answer
print(solve(n, A))
