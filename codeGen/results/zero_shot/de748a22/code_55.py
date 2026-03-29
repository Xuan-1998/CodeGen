import sys

n, q = map(int, input().split())
signs = list(input())

prefix_sum = [0] * (n + 1)
suffix_sum = [0] * (n + 1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + (1 if signs[i] == "+" else -1)
    suffix_sum[n-i-1] = suffix_sum[n-i] + (1 if signs[i] == "-" else -1)

for _ in range(q):
    l, r = map(int, input().split())
    query_sum = prefix_sum[r] - prefix_sum[l-1]
    if query_sum > 0:
        print(0)  # no need to remove any elements
    else:
        query_sum = suffix_sum[r] - suffix_sum[l-1]
        if query_sum < 0:
            print(-query_sum)  # need to remove all elements in this range
        else:
            print(query_sum)  # need to remove half of the elements in this range
