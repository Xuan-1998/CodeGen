# Define the function to find the length of the longest increasing subsequence
def longest_increasing_subsequence(arr):
    n = len(arr)
    
    # Initialize an array to store the lengths of the longest increasing subsequences ending at each position
    lis = [1] * n
    
    # Iterate over the array to fill up the lis array
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                # Update the length of the longest increasing subsequence ending at position i
                lis[i] = max(lis[i], lis[j] + 1)
    
    # Return the maximum length found
    return max(lis)

# Read input from stdin and write output to stdout
arr = list(map(int, input().split()))
print(longest_increasing_subsequence(arr))
