from sys import stdin

def can_reach_last_index(arr):
    last_index = len(arr) - 1
    current_index = 0
    
    while current_index < last_index:
        jump_length = arr[current_index]
        
        if current_index + jump_length > last_index:
            return False
        
        current_index += jump_length
    
    return True

arr = list(map(int, stdin.readline().split()))
print(can_reach_last_index(arr))
