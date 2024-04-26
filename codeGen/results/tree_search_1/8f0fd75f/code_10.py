import heapq
import sys

def read_input():
    n = int(input().strip())
    x = list(map(int, input().strip().split()))
    d = list(map(int, input().strip().split()))
    return n, x, d

def min_durability_required(n, x, d):
    # Calculate the spans for each point
    spans = [(min(d[i], x[i+1] - x[i]), min(d[i], x[i] - x[i-1])) for i in range(n)]
    
    # Create a heap to keep track of the weakest points
    heap = [(max(left, right), i) for i, (left, right) in enumerate(spans)]
    heapq.heapify(heap)
    
    # Process the weakest points
    while heap:
        max_span, i = heapq.heappop(heap)
        if max_span == 0:
            return 0  # No additional point is required
        
        # Check if the point can support the span without collapsing
        if max_span < spans[i][0] + spans[i][1]:
            # Collapse the point and redistribute the load
            if i > 0:
                spans[i-1] = (spans[i-1][0], spans[i-1][1] + spans[i][0])
                heapq.heappush(heap, (max(spans[i-1]), i-1))
            if i < n-1:
                spans[i+1] = (spans[i+1][0] + spans[i][1], spans[i+1][1])
                heapq.heappush(heap, (max(spans[i+1]), i+1))
        else:
            # The point can support the span, so add an additional point here
            return max_span - spans[i][0] - spans[i][1]

    # If we reach here, all points have been processed without collapsing
    return 0

# Read input from stdin
n, x, d = read_input()

# Calculate and print the answer
print(min_durability_required(n, x, d))
