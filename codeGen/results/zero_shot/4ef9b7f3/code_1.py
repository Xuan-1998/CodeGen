def find_eating_order(initial_queue, final_queue):
    i, j = 0, 0
    eating_order = []

    while i < len(initial_queue) and j < len(final_queue):
        sum_weights = initial_queue[i]
        i += 1
        # Find the consecutive monsters in the initial queue that sum up to the current monster in the final queue
        while i < len(initial_queue) and sum_weights < final_queue[j]:
            sum_weights += initial_queue[i]
            i += 1

        if sum_weights != final_queue[j]:
            return "NO", []

        # Simulate the eating process and record the order
        left = i - (sum_weights - initial_queue[i - 1])
        right = i - 1
        while left < right:
            if initial_queue[left] < initial_queue[right]:
                eating_order.append((right - left + 1, 'L'))
                initial_queue[left] += initial_queue[left + 1]
                left += 1
            else:
                eating_order.append((right - left + 1, 'R'))
                initial_queue[right] += initial_queue[right - 1]
                right -= 1

        j += 1

    if j != len(final_queue):
        return "NO", []

    return "YES", eating_order

# Read input from stdin
n = int(input())
initial_queue = list(map(int, input().split()))
k = int(input())
final_queue = list(map(int, input().split()))

# Process and output the result
result, eating_order = find_eating_order(initial_queue, final_queue)
print(result)
for order in eating_order:
    print(order[0], order[1])
