python
def binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

def count_valid_matrices(N, M):
    MOD = 998244353
    # Calculate the number of ways to choose 2 rows and 2 columns
    valid_matrices = binomial_coefficient(N + 1, 2) * binomial_coefficient(M + 1, 2)
    return valid_matrices % MOD

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

