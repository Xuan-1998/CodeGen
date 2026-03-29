import sys

def min_operations(arr):
    n = len(arr)
    swaps = 0
    inc_dec = 0
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            # Swap operation
            swaps += 1
        elif arr[i] < arr[i+1]:
            # Increase/decrease operation
            inc_dec += (arr[i+1] - arr[i]).abs()
    
    return swaps + inc_dec

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(min_operations(arr))
