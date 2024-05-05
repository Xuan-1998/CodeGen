from sys import stdin

def is_possible_to_reach_last_index(arr):
    current_position = 0
    max_jump_length = 0
    
    for i in range(len(arr)):
        if i > current_position and i <= current_position + arr[current_position]:
            current_position = i
        elif i > current_position:
            return False
        
        max_jump_length = max(max_jump_length, arr[i])
    
    return True

if __name__ == "__main__":
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    print(is_possible_to_reach_last_index(arr))
