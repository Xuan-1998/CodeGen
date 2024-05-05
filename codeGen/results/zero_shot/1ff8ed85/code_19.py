import sys

def can_send_sequence(b):
    # Calculate the sum of the elements in b
    total = sum(b)
    
    # Check if the sum is even (since we can split segments into two parts)
    if total % 2 != 0:
        return False
    
    # Initialize a variable to store the current segment length
    segment_length = 0
    
    # Iterate over the elements in b
    for num in b:
        # Add the current element to the segment length
        segment_length += num
        
        # If the segment length is greater than or equal to the next possible segment length,
        # reset the segment length and increment it by 1 (since we can't have a segment of length 0)
        if segment_length >= total // 2:
            segment_length = 1
        else:
            segment_length += 1
    
    # Return True if the final segment length is equal to total // 2,
    # indicating that b can be obtained from some sequence a
    return segment_length == total // 2

t = int(input())  # Read the number of test cases
for _ in range(t):
    n = int(input())  # Read the size of the sequence b
    b = list(map(int, input().split()))  # Read the sequence b
    
    if can_send_sequence(b):
        print("YES")
    else:
        print("NO")
