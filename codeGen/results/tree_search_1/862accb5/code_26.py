import sys

def read_input():
    n = int(input().strip())
    edges = [tuple(map(int, input().strip().split())) for _ in range(n)]
    return n, edges

def find_max_edge(edges):
    max_edge = max(edges, key=lambda x: x[2])
    return max_edge

def calculate_inconvenience(edges, max_edge):
    total_inconvenience = sum(weight for _, _, weight in edges)
    return total_inconvenience - max_edge[2]

def main():
    n, edges = read_input()
    max_edge = find_max_edge(edges)
    min_inconvenience = calculate_inconvenience(edges, max_edge)
    print(min_inconvenience)

if __name__ == "__main__":
    main()
