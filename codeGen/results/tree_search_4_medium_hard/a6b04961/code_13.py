import heapq
from collections import defaultdict

def max_hedgehogBeauty():
    n, m = map(int, input().split())
    edges = [(int(input()), *map(int, input().split())) for _ in range(m)]

    memo = defaultdict(int)
    memo[0] = 1  # Base case: one edge for no tail

    queue = [(edges[0][0], 0)]  # Initialize priority queue with the first edge
    last_vertex = 0

    while queue:
        distance, current_tail_length = heapq.heappop(queue)
        if current_tail_length > n - 1:  # Tail length exceeds maximum possible
            break

        for edge in edges:
            u, v = edge[1:]
            if u == last_vertex and edge[0] < distance:  # Edge can be added to the tail
                new_tail_length = current_tail_length + 1
                memo[new_tail_length] = max(memo.get(new_tail_length, 0), memo[current_tail_length] * (new_tail_length - current_tail_length))
                heapq.heappush(queue, (edge[0], new_tail_length))  # Add edge to the priority queue

        last_vertex += 1  # Move to the next vertex in the tail

    return max(memo.values())

print(max_hedgehogBeauty())
