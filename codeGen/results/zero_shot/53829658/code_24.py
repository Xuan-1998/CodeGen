from collections import defaultdict

def read_input():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        si, ti = map(int, input().split())
        graph[si].append(ti)
    return n, graph

def find_capital(graph):
    capital_cities = []
    min_edges_to_reverse = float('inf')
    for city in range(1, len(graph)):
        edges_to_reverse = 0
        for neighbor in graph[city]:
            if neighbor not in graph:
                edges_to_reverse += 1
        if edges_to_reverse < min_edges_to_reverse:
            min_edges_to_reverse = edges_to_reverse
            capital_cities = [city]
        elif edges_to_reverse == min_edges_to_reverse:
            capital_cities.append(city)
    return min_edges_to_reverse, capital_cities

def main():
    n, graph = read_input()
    min_edges_to_reverse, capital_cities = find_capital(graph)
    print(min_edges_to_reverse)
    for city in sorted(capital_cities):
        print(city)

if __name__ == "__main__":
    main()
