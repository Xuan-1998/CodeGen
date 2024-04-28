import sys
from collections import deque

def solve():
    N = int(input())
    nums = [int(x) for x in input().split()]

    # Create a graph with 2^n nodes, where n is the number of integers
    graph = {}
    for subset_len in range(N + 1):
        node_id = (1 << subset_len) - 1  # Binary representation of the subset length
        graph[node_id] = []

        for mask in range(1 << N):  # Iterate over all subsets of length subset_len
            if (mask & node_id) == node_id:  # If this subset has the correct length
                sum_val = 0
                for i in range(N):
                    if (mask >> i) & 1:
                        sum_val += nums[i]

                # Add an edge to the graph with weight equal to the sum of the integers
                graph[node_id].append((sum_val, mask))

    # Apply Dijkstra's algorithm to find all shortest paths (sums)
    shortest_sums = set()
    queue = deque([(0, 0)])  # Initialize with the empty subset and sum

    while queue:
        curr_sum, node_id = queue.popleft()

        for neighbor_sum, neighbor_mask in graph[node_id]:
            new_sum = curr_sum + neighbor_sum
            if new_sum not in shortest_sums:
                shortest_sums.add(new_sum)
                queue.append((new_sum, neighbor_mask))

    # Print the result as a space-separated list of integers
    print(' '.join(map(str, sorted(list(shortest_sums)))))

if __name__ == '__main__':
    solve()
