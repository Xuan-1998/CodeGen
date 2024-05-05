import math

def read_input():
    T = int(input())
    for _ in range(T):
        n, *edges = [int(x) for x in input().split()]
        m, *prime_factors = [int(x) for x in input().split()]
        prime_factors.sort()
        k = 1
        for factor in prime_factors:
            k *= factor

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        product = 1
        for i, j in edges:
            dp[i][j] = math.gcd(k // product, product)
            product *= dp[i][j]
        return n, edges, m, prime_factors

def solve():
    T = int(input())
    for _ in range(T):
        n, edges, m, prime_factors = read_input()
        # Your dynamic programming logic goes here
        pass

if __name__ == "__main__":
    solve()
