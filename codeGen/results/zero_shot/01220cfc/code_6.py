import sys

def canReachLastIndex(arr):
    n = len(arr)
    last_index_reachable = n - 1
    
    for i in range(n-2, -1, -1):
        if arr[i] >= i + 1:
            last_index_reachable = i
        else:
            break
            
    return bool(last_index_reachable == n - 1)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(canReachLastIndex(arr))
