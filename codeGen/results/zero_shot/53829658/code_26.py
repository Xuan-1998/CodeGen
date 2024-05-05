import sys

def read_input():
    n = int(sys.stdin.readline())
    roads = []
    for _ in range(n-1):
        si, ti = map(int, sys.stdin.readline().split())
        roads.append((si, ti))
    return n, roads

def find_optimal_capital(roads):
    # Use DFS or topological sorting to traverse the graph
    # and find the root node (capital city)
    capital_city = None
    for road in roads:
        si, ti = road
        if not capital_city:  # Root node is the first city
            capital_city = si
        else:
            capital_city = max(capital_city, si)  # Update capital city if needed

    return capital_city

def main():
    n, roads = read_input()
    capital_city = find_optimal_capital(roads)
    print(min_edges_to_invert(n, roads, capital_city))  # Print the minimum number of edges to invert
    print(capital_city)  # Print all possible ways to choose the capital

def min_edges_to_invert(n, roads, capital_city):
    # Calculate the minimum number of edges to invert
    pass  # TO DO: Implement this function

if __name__ == "__main__":
    main()
