from collections import defaultdict, deque
import sys

def find_order(n, prerequisites):
    in_degree = [0] * n
    graph = defaultdict(list)
    for i in range(n):
        for prereq in prerequisites[i]:
            graph[prereq].append(i)
            in_degree[i] += 1
    return in_degree, graph

def topological_sort(n, in_degree, graph):
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) == n:
        return order
    else:
        return None

def min_times_to_read_book(n, prerequisites):
    in_degree, graph = find_order(n, prerequisites)
    order = topological_sort(n, in_degree, graph)
    if order is None:
        return -1
    levels = [0] * n
    for node in order:
        for neighbor in graph[node]:
            levels[neighbor] = max(levels[neighbor], levels[node] + 1)
    return max(levels) + 1

# Read input and process test cases
def main():
    input_lines = sys.stdin.readlines()
    line_index = 0
    while line_index < len(input_lines):
        n = int(input_lines[line_index].strip())
        line_index += 1
        prerequisites = []
        for i in range(n):
            line = list(map(int, input_lines[line_index].strip().split()))
            prerequisites.append(line[1:])
            line_index += 1
        result = min_times_to_read_book(n, prerequisites)
        print(result)

if __name__ == "__main__":
    main()
