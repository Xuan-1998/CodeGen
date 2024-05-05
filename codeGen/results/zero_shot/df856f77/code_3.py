import sys

def min_operations(arr):
    n = len(arr)
    min_val = arr[0]
    ops = 0
    
    for i in range(1, n):
        if arr[i] <= min_val:
            ops += min_val - arr[i] + 1
            min_val = arr[i]
    
    return ops

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    print(min_operations(arr))
