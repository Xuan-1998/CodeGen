def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    m = int(input())
    prime_factors = list(map(int, input().split()))

    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n):
        dp[i][i] = 1

    prefix_products = [1] * (n+1)
    suffix_products = [1] * (n+1)

    for u, v in edges:
        prefix_products[v] *= prefix_products[u]
        suffix_products[v] *= suffix_products[v-1]

    distribution_index = sum(prefix_products[i] * suffix_products[i] for i in range(2, n))

    return distribution_index % (10**9 + 7)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(solve())
