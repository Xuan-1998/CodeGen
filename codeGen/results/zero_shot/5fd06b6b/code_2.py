import heapq

def min_sum_of_counts(n, counts):
    counts.reverse()
    queue = []
    for count in counts:
        if not queue or count > -queue[0]:
            heapq.heappush(queue, -count)
        else:
            heapq.heappushpop(queue, -count - 1)
    return -sum(queue)

n = int(input().strip())
counts = list(map(int, input().strip().split()))
print(min_sum_of_counts(n, counts))

