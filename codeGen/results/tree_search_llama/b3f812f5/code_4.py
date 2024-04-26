def find_indices(Arr):
    # Create an empty dictionary (hash map) to store the matching indices
    index_map = {}
    
    # Iterate through the array and check if each element is equal to its index
    for i, val in enumerate(Arr):
        if i + 1 == val:  # Note the addition of 1 for 1-based indexing
            index_map[val] = i
    
    # Return a list comprehension containing the indices where Arr[i] = i
    return [i for i in index_map.values() if i >= 0]

# Test your solution with example inputs
N = int(input())  # Input the number of elements in the array
Arr = list(map(int, input().split()))  # Read the array from standard input

print(find_indices(Arr))
