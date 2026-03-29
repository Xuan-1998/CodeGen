def main():
    T = int(input())
    for _ in range(T):
        n, m, k = [int(x) for x in input().split()]
        p1, p2, ..., pm = [int(x) for x in input().split()]
        edges = []
        for i in range(n-1):
            u, v = [int(x) for x in input().split()]
            edges.append((u, v))
        adj_list = preprocess_tree(edges, n)
        dist_idx = calc_distribution_index(adj_list, edges)
        print(dist_idx % (10**9 + 7))

if __name__ == "__main__":
    main()
