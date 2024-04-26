from collections import deque
import sys

def min_reads_to_understand_book(num_chapters, prerequisites):
    # Create an adjacency list and in-degree array
    adj_list = {i: [] for i in range(1, num_chapters + 1)}
    in_degree = {i: 0 for i in range(1, num_chapters + 1)}
    
    # Fill the adjacency list and in-degree array
    for chapter, reqs in prerequisites.items():
        for req in reqs:
            adj_list[req].append(chapter)
            in_degree[chapter] += 1
    
    # Initialize a queue with all chapters with zero in-degree
    queue = deque([chapter for chapter in in_degree if in_degree[chapter] == 0])
    read_count = 0
    
    while queue:
        next_queue = deque()
        while queue:
            chapter = queue.popleft()
            for next_chapter in adj_list[chapter]:
                in_degree[next_chapter] -= 1
                if in_degree[next_chapter] == 0:
                    next_queue.append(next_chapter)
        queue = next_queue
        read_count += 1
    
    # If there are chapters with non-zero in-degree, return -1
    if any(in_degree.values()):
        return -1
    return read_count

# Read input from stdin
def main():
    input_data = sys.stdin.readlines()
    iterator = iter(input_data)
    t = int(next(iterator))  # Number of test cases
    
    for _ in range(t):
        num_chapters = int(next(iterator))
        prerequisites = {}
        for i in range(1, num_chapters + 1):
            line = list(map(int, next(iterator).split()))
            prerequisites[i] = line[1:]
        
        # Calculate and print the result
        print(min_reads_to_understand_book(num_chapters, prerequisites))

if __name__ == "__main__":
    main()
