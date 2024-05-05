import heapq

def max_gasoline():
    n = int(input())
    gasolines = list(map(int, input().split()))
    roads = []
    for _ in range(n-1):
        u, v, c = map(int, input().split())
        roads.append((c, u, v))

    # Sort the roads by length
    roads.sort()

    # Initialize the heap with all cities as starting points
    heap = [(gasolines[i], i) for i in range(n)]
    heapq.heapify(heap)

    max_gasoline = 0

    while heap:
        gas, city = heapq.heappop(heap)
        if gas > max_gasoline:
            max_gasoline = gas
            # Add all the roads to visit that start from this city
            for c in range(n):
                if c != city and roads[0][0] <= gasolines[c]:
                    heapq.heappush(heap, (gas - c, c))
                    break

    return max_gasoline

print(max_gasoline())
