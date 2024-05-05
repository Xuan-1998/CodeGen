import heapq

def min_cost_to_sort_strings(costs, strings):
    # Create a priority queue to store the nodes (strings)
    pq = []
    for i in range(len(strings)):
        # Calculate the initial cost for each string (its own length)
        init_cost = len(strings[i])
        heapq.heappush(pq, (init_cost, i))

    sorted_strings = []
    while pq:
        # Extract the node with the minimum cost
        _, idx = heapq.heappop(pq)

        # Initialize the current string and its cost
        curr_string = strings[idx]
        curr_cost = costs[idx]

        # Try to move the string to the next possible position by reversing it
        for j in range(len(curr_string)):
            rev_string = curr_string[::-1][j:]
            if rev_string not in sorted_strings:
                # Add the new string and its cost to the priority queue
                heapq.heappush(pq, (curr_cost + len(rev_string), len(sorted_strings)))
                sorted_strings.append(rev_string)
                break

    return -1 if len(sorted_strings) != len(strings) else sum(costs)

# Example usage:
n = int(input())  # Read the number of strings
costs = [int(input()) for _ in range(n)]  # Read the costs for each string
strings = [input() for _ in range(n)]  # Read the strings themselves

min_cost = min_cost_to_sort_strings(costs, strings)
print(min_cost)  # Output the minimum total cost required to sort the strings
