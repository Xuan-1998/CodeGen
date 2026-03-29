import sys

def min_operations(arr):
    n = len(arr)
    inversions = 0
    
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                inversions += 1
    
    return inversions

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    
    min_ops = min_operations(arr)
    
    print(min_ops)
