from collections import defaultdict

def treeland(n, roads):
    # Initialize graph as an adjacency list
    graph = defaultdict(list)
    
    # Add edges to the graph
    for road in roads:
        si, ti = map(int, road.split())
        graph[si].append(ti)
        
    # Calculate in-degrees and out-degrees of each city
    in_degrees = [0] * (n + 1)
    out_degrees = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for neighbor in graph[i]:
            in_degrees[neighbor] += 1
            out_degrees[i] += 1
            
    # Find the maximum in-degree to determine the optimal capital
    max_in_degree = max(in_degrees)
    
    # Initialize dp array with base case being 0
    dp = [0] * (n + 1)
    
    # Calculate the minimum number of reversed roads for each city
    for i in range(2, n + 1):
        for neighbor in graph[i]:
            if in_degrees[neighbor] == max_in_degree:
                dp[i] = max(dp[i], dp[neighbor - 1] + 1)
    
    # Return the maximum value and print it along with the optimal capital
    return max(dp), max_in_degree

n = int(input())
roads = []
for _ in range(n - 1):
    roads.append(list(map(int, input().split())))
min_reversed_roads, optimal_capital = treeland(n, roads)
print(min_reversed_roads)
print(optimal_capital + 1)  # Add 1 to include the capital city
