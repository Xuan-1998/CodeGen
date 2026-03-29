import sys

def max_xor_sum(n, x, arr):
    # Sort the array in ascending order
    arr.sort()

    # Calculate the prefix sums of the sorted array
    prefix_sums = [0]
    for i in range(1, n):
        prefix_sums.append(prefix_sums[-1] + arr[i])

    # Initialize the maximum sum
    max_sum = 0

    # Iterate through the prefix sums and calculate the maximum sum
    for i in range(n - 1):
        max_sum = max(max_sum, prefix_sums[i + 1] - prefix_sums[i] + x)

    return max_sum


# Read input from stdin
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Calculate and print the maximum sum
    max_sum = max_xor_sum(n, x, arr)
    print(max_sum)
