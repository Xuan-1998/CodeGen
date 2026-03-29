import sys

def min_operations(arr):
    n = len(arr)
    max_val = arr[-1]
    operations = 0
    
    for i in range(n-2, -1, -1):
        while arr[i] > max_val:
            max_val -= 1
            operations += 1
        max_val = arr[i]
    
    print(operations)

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    min_operations(arr)
