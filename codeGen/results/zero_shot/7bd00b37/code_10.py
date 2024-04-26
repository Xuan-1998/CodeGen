import sys
from collections import defaultdict

MOD = 998244353

def read_input():
    n = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    return n, edges

def construct_tree(n, edges):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    return tree

def main():
    n, edges = read_input()
    tree = construct_tree(n, edges)
    # TODO: Implement the dynamic programming solution

if __name__ == "__main__":
    main()
