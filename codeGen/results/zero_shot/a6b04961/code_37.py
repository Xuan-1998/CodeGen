import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, edges

def find_max_beauty(n, m, edges):
    # implement the DFS algorithm to find all possible tails
    # and count the number of spines for each tail
    pass

if __name__ == "__main__":
    n, m, edges = read_input()
    max_beauty = 0
    # implement the logic to find the maximum beauty
    print(max_beauty)
