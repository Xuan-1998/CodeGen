import sys

n, q = map(int, input().split())
signs = list(input())

prefix_sum = [0] * (n + 1)
suffix_sum = [0] * (n + 1)

for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + signs[i]
    suffix_sum[n - i - 1] = suffix_sum[n - i] - signs[n - i - 1]

for _ in range(q):
    l, r = map(int, input().split())
    
    # Calculate the sum of the elements in the range
    range_sum = prefix_sum[r] - prefix_sum[l - 1]
    
    # Initialize the count of elements that can be removed
    count = 0
    
    # Iterate over the range and find the minimal number of elements that can be removed
    for i in range(l, r + 1):
        if signs[i] == signs[i]:
            count += 1
    
    print(count)
