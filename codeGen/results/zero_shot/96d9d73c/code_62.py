import sys
from collections import defaultdict

def can_partition(n, k, m, arr):
    # Sort the array
    arr.sort()
    
    # Create a hashmap to store the count of elements at each index modulo M
    count = defaultdict(int)
    for num in arr:
        count[num % m] += 1
    
    # Initialize a variable to keep track of the maximum value seen so far
    max_val = 0
    
    # Iterate over the hashmap to find the maximum value and calculate the total number of partitions required
    for key, val in count.items():
        if val > 0:
            max_val = max(max_val, min(val, (m - 1) // (key + 1)) * k)
    
    # Calculate the actual number of elements that would be used up
    actual_used = sum(min(num % m, k) for num in arr)
    
    # Check if it's possible to partition the array according to the given rules
    return actual_used <= max_val

if __name__ == "__main__":
    n, k, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(can_partition(n, k, m, arr))
