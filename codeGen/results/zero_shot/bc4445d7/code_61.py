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
        
        max_distribution_index = find_max_distribution_index(n, edges, prime_factors)
        print(max_distribution_index)

if __name__ == "__main__":
    main()
