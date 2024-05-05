import heapq
from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    i = 2
    while n > 1:
        if is_prime(i) and n % i == 0:
            factors.append((i, 1))
            n //= i
        else:
            i += 1
    return [x[0] for x in sorted(factors)]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []
        for _ in range(n - 1):
            u, v = map(int, input().split())
            edges.append((u, v))
        m = int(input())
        prime_factors_list = prime_factors(2 ** (m + 4))[:m]
        k = 1
        for p in prime_factors_list:
            k *= p
        edge_labels = []
        for u, v in edges:
            if is_prime(k):
                edge_labels.append(k)
                k //= k
            else:
                i = 0
                while k % prime_factors_list[i][0] != 0:
                    i += 1
                edge_labels.append(prime_factors_list[i][0])
                k //= prime_factors_list[i][0]
        path_sums = {}
        for u, v in edges:
            if (u, v) not in path_sums:
                path_sums[(u, v)] = edge_labels[edges.index((u, v))]
            for w in range(1, n):
                if (w, u) in path_sums and (w, v) in path_sums:
                    path_sums[(u, v)] += path_sums[(w, u)] + path_sums[(w, v)]
        distribution_index = sum(sum(path_sums.values()))
        print(distribution_index % (10 ** 9 + 7))

if __name__ == "__main__":
    main()
