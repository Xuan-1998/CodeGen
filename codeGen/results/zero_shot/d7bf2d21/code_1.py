import sys
from collections import defaultdict

# Read the array of integers from stdin
arr = list(map(int, sys.stdin.readline().split()))

# Initialize a dictionary to store the length of longest increasing subsequence ending at each element
lis_dict = defaultdict(int)

for i in range(len(arr)):
    # Find the maximum length of increasing subsequence ending at arr[i]
    max_lis = 0
    for j in range(i):
        if arr[i] > arr[j]:
            max_lis = max(max_lis, lis_dict[j])
    # Update the dictionary with the maximum length found
    lis_dict[i] = max_lis + 1

# Count the number of longest increasing subsequences using the dictionary
max_lis_length = max(lis_dict.values())
count = sum(1 for k in lis_dict if lis_dict[k] == max_lis_length)

print(count)
