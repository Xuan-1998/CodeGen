import sys

def min_operations(arr):
    n = len(arr)
    operations = 0
    
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        
        if diff > 0:  # element is smaller than the next one
            operations += diff
            arr[i+1] -= diff
    
    return operations

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(min_operations(arr))
