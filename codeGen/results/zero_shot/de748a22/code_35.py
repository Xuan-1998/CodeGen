def process_query(cum_sum, l, r):
    left_sum = cum_sum[r] - cum_sum[l - 1]
    if left_sum == 0:  # If the sum is already zero, no elements need to be removed.
        return 0
    right_sum = cum_sum[-1] - cum_sum[r]
    if right_sum == 0:  # If the sum of remaining elements is zero, no elements need to be removed.
        return 0
    min_removed = float('inf')
    for i in range(l - 1, r):
        left_sum -= signs[i]
        right_sum += signs[i]
        if left_sum == 0:  # If the sum of remaining elements is zero, this is the minimal number of elements that need to be removed.
            min_removed = min(min_removed, r - i)
    return min_removed

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(process_query(cum_sum, l, r))
