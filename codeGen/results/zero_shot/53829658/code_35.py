import heapq

def read_input():
    n = int(input())
    roads = []
    for _ in range(n-1):
        si, ti = map(int, input().split())
        roads.append((si, ti))
    return n, roads

def calculate_distances(n, roads):
    graph = [[] for _ in range(n+1)]
    for si, ti in roads:
        graph[si].append(ti)
    distances = [float('inf')] * (n+1)
    distances[0] = 0
    pq = [(0, 0)]
    while pq:
        d, city = heapq.heappop(pq)
        if d > distances[city]:
            continue
        for neighbor in graph[city]:
            distance = d + 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

def choose_capital(distances):
    median_distance = distances[len(distances)//2]
    capital_city = -1
    for city in range(1, len(distances)):
        if distances[city] == median_distance:
            capital_city = city
            break
    return capital_city

def calculate_inverse_roads(n, roads, capital_city):
    inverse_roads = 0
    for si, ti in roads:
        if si != capital_city and ti != capital_city:
            if ti < si:
                si, ti = ti, si
            if si == capital_city or ti == capital_city:
                continue
            else:
                inverse_roads += 1
    return inverse_roads

def main():
    n, roads = read_input()
    distances = calculate_distances(n, roads)
    capital_city = choose_capital(distances)
    inverse_roads = calculate_inverse_roads(n, roads, capital_city)
    print(inverse_roads)
    print(capital_city)

if __name__ == "__main__":
    main()

