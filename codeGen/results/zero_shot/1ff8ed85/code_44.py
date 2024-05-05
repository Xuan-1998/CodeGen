import sys

def can_send_over_network(b):
    n = len(b)
    
    # Check if all elements are consecutive
    if not (b[0] == 1 or b[0] - 1 == min(b) and max(b) == n):
        return "NO"
    
    for i in range(n):
        segment_length = b[i]
        remaining_elements = n - segment_length
        
        # Check if remaining elements are consecutive
        if not (remaining_elements == 0 or min(remaining_elements, b[0] - 1) + max(b) - segment_length == n and min(b[0], remaining_elements) - 1 == min(min(b), remaining_elements)):
            return "NO"
    
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    print(can_send_over_network(b))
