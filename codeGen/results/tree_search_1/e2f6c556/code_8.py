from collections import deque
import sys

def min_reads_to_understand_book(n, prerequisites):
    indegree = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]

    # Create the adjacency list and indegree list
    for chapter, prereq in prerequisites.items():
        for pre in prereq:
            adj_list[pre].append(chapter)
            indegree[chapter] += 1

    # Topological sort with cycle detection
    queue = deque()
    for chapter in range(1, n + 1):
        if indegree[chapter] == 0:
            queue.append(chapter)

    read_count = 0
    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            for dependent in adj_list[current]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)
        read_count += 1

    # Check if all chapters are processed
    if sum(indegree) == 0:
        return read_count
    else:
        return -1

def main():
    input_data = sys.stdin.readlines()
    iterator = iter(input_data)
    test_cases = int(next(iterator))
    
    for _ in range(test_cases):
        n = int(next(iterator))
        prerequisites = {}
        for i in range(1, n + 1):
            line = list(map(int, next(iterator).split()))
            prerequisites[i] = line[1:]
        result = min_reads_to_understand_book(n, prerequisites)
        print(result)

if __name__ == "__main__":
    main()
