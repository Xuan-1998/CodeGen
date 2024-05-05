import heapq

def min_operations():
    T = int(input())  # number of test cases
    for _ in range(T):
        n = int(input())  # number of vertices
        parent = [0] * (n + 1)  # parent array
        ranges = []  # list of vertex ranges

        # read input data
        for i in range(n - 1):
            p, _ = map(int, input().split())
            parent[p] = i
        for i in range(1, n + 1):
            l, r = map(int, input().split())
            ranges.append((l, r))

        # initialize priority queue with root vertex
        pq = [(0, 0)]  # (value, vertex index)
        while pq:
            value, vertex = heapq.heappop(pq)

            # update values for ancestors of current vertex
            while vertex > 0:
                parent_vertex = parent[vertex]
                ranges[parent_vertex] = max(ranges[parent_vertex], min(value + r - l, r))
                if parent_vertex > 0:
                    heapq.heappush(pq, (ranges[parent_vertex][0], parent_vertex))
                vertex = parent_vertex

        # print the minimum number of operations
        print(sum((r[1] - r[0]) for r in ranges))

min_operations()
