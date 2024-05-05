from collections import deque

def can_reach(arr):
    memo = {}
    queue = deque([(0, False)])  # Initialize the queue with the starting index (0) and a flag indicating whether we've reached the last index or not

    while queue:
        i, max_reached = queue.popleft()

        if i >= len(arr) - 1:  # If we've reached the last index
            return True

        if i in memo:
            continue

        max_reachable = False
        for j in range(min(i + arr[i] + 1, len(arr)), 0, -1):
            if can_reach((j, False)) and j <= i + arr[i]:
                max_reachable = True
                break

        memo[i] = max_reachable
        if not max_reachable:
            continue
        queue.append((i + 1, max_reached or max_reachable))  # Add the next index to the queue with its corresponding flag

    return False  # If we haven't reached the last index after iterating through all indices, it's impossible to reach the last index

# Read input from standard input
arr = list(map(int, input().split()))

if can_reach(arr):
    print("Possible")
else:
    print("Impossible")
