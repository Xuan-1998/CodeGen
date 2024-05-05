import sys

def min_operations(arr):
    arr = list(map(int, input().split()))
    n = len(arr)
    min_ops = 0
    max_val = arr[0]
    
    for i in range(1, n):
        if arr[i] <= max_val:
            min_ops += (max_val - arr[i]) + 1
            max_val = arr[i] + 1
    
    print(min_ops)

if __name__ == "__main__":
    min_operations(sys.stdin.read().split())
