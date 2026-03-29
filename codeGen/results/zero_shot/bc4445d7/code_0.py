def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        edges = [(u, v) for u, v in zip(*[map(int, input().split()) for _ in range(n - 1)])]
        m = int(input())
        prime_factors = [int(x) for x in input().split()]
        k = math.prod(prime_factors)
        tree = build_tree(edges)
        max_di = max_distribution_index(tree)
        print(max_di % (10**9 + 7))

if __name__ == '__main__':
    main()
