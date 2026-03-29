import sys

def is_jump_possible(arr):
    n = len(arr)
    max_reach = 0
    
    for i in range(n - 1, -1, -1):
        if arr[i] > i - max_reach:
            max_reach = i
        else:
            return False
    
    return True

n = int(input())
arr = list(map(int, input().split()))
print(is_jump_possible(arr))
