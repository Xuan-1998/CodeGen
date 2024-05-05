import sys

def min_operations(arr):
    n = len(arr)
    ops = 0
    
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            diff = arr[i] - arr[i+1]
            ops += abs(diff) + 1
    
    return ops

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    print(min_operations(arr))
