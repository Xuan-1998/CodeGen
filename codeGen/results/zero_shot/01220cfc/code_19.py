def can_reach_last_index(arr):
    current_pos = 0
    max_jump = arr[0]
    
    for i in range(1, len(arr)):
        if i <= max_jump:
            current_pos = i
            max_jump = min(max_jump, arr[i])
        else:
            return False
    
    return True

if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(can_reach_last_index(arr))
