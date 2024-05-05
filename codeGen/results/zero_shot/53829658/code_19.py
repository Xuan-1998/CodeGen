import sys

def main():
    n = int(sys.stdin.readline())
    roads = []
    for _ in range(n-1):
        si, ti = map(int, sys.stdin.readline().split())
        roads.append((si-1, ti-1))  # subtract 1 to make indexing 0-based
    
    capital_cities = set(range(n))
    min_edges_to_reverse = float('inf')
    optimal_capital_city = None
    
    for city in capital_cities:
        edges_to_reverse = 0
        current_city = city
        visited = {city}
        
        while True:
            for neighbor in roads:
                if neighbor[1] == current_city and neighbor[0] not in visited:
                    edges_to_reverse += 1
                    visited.add(neighbor[0])
                    current_city = neighbor[0]
                    break
            else:
                break
        
        if edges_to_reverse < min_edges_to_reverse:
            min_edges_to_reverse = edges_to_reverse
            optimal_capital_city = city
    
    print(min_edges_to_reverse)
    print(*[i+1 for i in range(n)], sep=' ')

if __name__ == "__main__":
    main()
