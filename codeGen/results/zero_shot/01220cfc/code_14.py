# Step 1: Read the input array
input_array = list(map(int, input().split()))
length = len(input_array)

# Step 2: Initialize two pointers, one at the start of the array and one at the end
start = 0
end = length - 1

# Step 3: Iterate through the array from both ends
while start <= end:
    # Check if it's possible to reach the current position from the start or end
    if (input_array[start] >= input_array[end]):
        # If yes, move towards the center of the array
        mid = (start + end) // 2
        if (mid < length - 1 and input_array[mid] >= input_array[mid + 1]):
            return False
        start = mid + 1
    else:
        # If no, move towards the other end
        end = mid

# Step 4: Return True if it's possible to reach the last index, False otherwise
return start >= length - 1
