from collections import defaultdict

def main():
    n = int(input())
    graph = defaultdict(list)
    for i in range(1, n):
        u, v = map(int, input().split())
        graph[u].append(v)

    # Find the capital city with the minimum number of reversals
    min_reversals = float('inf')
    capital_city = None
    for city in range(1, n):
        reversals = 0
        current_city = city
        visited = set()
        while True:
            if current_city not in visited:
                visited.add(current_city)
                for neighbor in graph[current_city]:
                    if neighbor not in visited:
                        current_city = neighbor
                        break
            else:
                break
        reversals += len(visited) - 1
        if reversals < min_reversals:
            min_reversals = reversals
            capital_city = city

    # Print the minimum number of roads to be inversed and all possible ways to choose the capital
    print(min_reversals)
    for i in range(1, n):
        if i != capital_city:
            graph[i].reverse()
    for city in range(1, n):
        visited = set()
        current_city = city
        while True:
            if current_city not in visited:
                visited.add(current_city)
                for neighbor in graph[current_city]:
                    if neighbor not in visited:
                        current_city = neighbor
                        break
            else:
                break
        print(*visited, sep=' ')

if __name__ == "__main__":
    main()
