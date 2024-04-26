def find_bridges(n, roads):
    # Implement a function to find all bridges in the graph
    pass

def calculate_inconvenience(roads, bridge_roads):
    # Implement a function to calculate the total inconvenience after removing a road
    pass

def main():
    n = int(input().strip())
    roads = []
    for _ in range(n):
        u, v, l = map(int, input().split())
        roads.append((u, v, l))
    
    bridge_roads = find_bridges(n, roads)
    result = calculate_inconvenience(roads, bridge_roads)
    
    print(result)

if __name__ == "__main__":
    main()
