import sys

def min_operations(arr):
    arr.sort()  # O(n log n) time complexity
    
    operations = 0
    for i in range(len(arr) - 1):
        diff = arr[i+1] - arr[i]
        if diff > 0:
            operations += diff
        elif diff < 0:
            operations -= diff
    
    return operations

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    
    print(min_operations(arr))
