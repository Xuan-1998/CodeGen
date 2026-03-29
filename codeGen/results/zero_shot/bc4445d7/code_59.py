def find_prime_factors(k):
    factors = []
    i = 2
    while i * i <= k:
        if k % i:
            i += 1
        else:
            k //= i
            factors.append(i)
    if k > 1:
        factors.append(k)
    return factors

def calculate_distribution_index(edges, labels):
    n = len(edges) + 1
    distribution_index = 0
    for i in range(n-1):
        for j in range(i+1, n):
            f_ij = 1
            path_edges = []
            while i != j:
                u, v = edges[i]
                if u == i:
                    f_ij *= labels[i]
                elif v == i:
                    f_ij *= labels[i-1]
                i = v
                path_edges.append((u, v))
            distribution_index += sum(f_path for f_path in (labels[path_edge[0]] if path_edge[0] == i else labels[path_edge[1]-1] for path_edge in path_edges))
    return distribution_index

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        edges = []
        for _ in range(n-1):
            u, v = map(int, input().split())
            edges.append((u, v))
        m = int(input())
        prime_factors = list(map(int, input().split()))
        k = 1
        for factor in prime_factors:
            k *= factor
        labels = [0] * (n-1)
        for edge in edges:
            product_of_all_edge_labels = 1
            while product_of_all_edge_labels % k == 0:
                product_of_all_edge_labels += 1
            labels[edges.index(edge)] = product_of_all_edge_labels
        distribution_index = calculate_distribution_index(edges, labels)
        print(distribution_index % (10**9 + 7))

if __name__ == "__main__":
    main()
