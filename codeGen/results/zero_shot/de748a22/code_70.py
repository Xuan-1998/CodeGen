import sys

n, q = map(int, input().split())
signs = list(map(lambda x: 1 if x == "+" else -1, input()))

cumulative_sum = [0]
for sign in signs:
    cumulative_sum.append(cumulative_sum[-1] + sign)

for _ in range(q):
    l, r = map(int, input().split())
    left_sum = cumulative_sum[r]
    right_sum = cumulative_sum[l-1]

    # Find the minimum number of elements to remove
    min_remove = (left_sum - right_sum) // 2
    if (left_sum - right_sum) % 2:
        min_remove += 1

    print(min_remove)
