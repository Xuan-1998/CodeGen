from collections import defaultdict, deque
import sys

def find_longest_path(n, graph):
    in_degree = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in graph[i]:
            in_degree[j] += 1

    # Perform topological sorting using Kahn's algorithm
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    longest_path = [0] * (n + 1)
    count_visited = 0
    while queue:
        node = queue.popleft()
        count_visited += 1
        for next_node in graph[node]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                queue.append(next_node)
            longest_path[next_node] = max(longest_path[next_node], longest_path[node] + 1)

    # If count_visited is not equal to n, there is a cycle
    if count_visited != n:
        return -1

    return max(longest_path) + 1

def main():
    input_data = sys.stdin.readlines()
    line_index = 0
    test_cases = int(input_data[line_index].strip())
    line_index += 1

    for _ in range(test_cases):
        n = int(input_data[line_index].strip())
        line_index += 1
        graph = defaultdict(list)
        for i in range(1, n + 1):
            line = list(map(int, input_data[line_index].strip().split()))
            line_index += 1
            for j in line[1:]:
                graph[j].append(i)  # Reverse the graph to make it easier to find the longest path

        result = find_longest_path(n, graph)
        print(result)

if __name__ == "__main__":
    main()
