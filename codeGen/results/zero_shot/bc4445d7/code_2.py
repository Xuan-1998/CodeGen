import sys

def solve():
    n = int(sys.stdin.readline())
    adj_list = [[] for _ in range(n)]
    for i in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    m = int(sys.stdin.readline())
    prime_factors = list(map(int, sys.stdin.readline().split()))
    k = 1
    for p in prime_factors:
        k *= p

    edge_labels = [k // p for p in prime_factors]
    total_ones = sum(1 for label in edge_labels if label == 1)
    max_distribution_index = total_ones * (n-2) + n*(n-3)//2
    print(max_distribution_index % (10**9 + 7))

if __name__ == "__main__":
    solve()
