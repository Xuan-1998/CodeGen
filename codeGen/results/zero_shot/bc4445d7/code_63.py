n = int(input())
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

m = int(input())
prime_factors = list(map(int, input().split()))
k = 1
for prime in prime_factors:
    k *= prime

total_edges = n - 1
total_prime = m

max_distribution_index = total_edges * k

print(max_distribution_index % (10**9 + 7))
