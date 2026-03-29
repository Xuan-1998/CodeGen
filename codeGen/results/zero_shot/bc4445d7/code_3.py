T = int(input())
for _ in range(T):
    n = int(input())
    m = int(input())
    p = list(map(int, input().split()))
    edge_labels = generate_edge_labels(n, m, p)
    max_index = max([max_distribution_index(edge_label) for edge_label in edge_labels])
    print(max_index)
