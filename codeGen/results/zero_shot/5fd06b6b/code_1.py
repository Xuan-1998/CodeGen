import heapq

def min_sum(n, sequence):
    # Initialize the sum and the priority queue
    sum_counts = 0
    queue = [-sequence[0]]

    # Iterate over the sequence
    for i in range(1, n):
        # If the current element is greater than the max in the queue, push it into the queue
        if -queue[0] < sequence[i]:
            heapq.heappush(queue, -sequence[i])
        # If the current element is less than or equal to the max in the queue, pop the max, add it to the sum, and push the current element
        else:
            sum_counts += -heapq.heappop(queue)
            heapq.heappush(queue, -sequence[i])

    # Add the remaining elements in the queue to the sum
    while queue:
        sum_counts += -heapq.heappop(queue)

    return sum_counts

n = int(input().strip())
sequence = list(map(int, input().strip().split()))
print(min_sum(n, sequence))

