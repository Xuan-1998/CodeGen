import sys

def min_operations(arr):
    N = len(arr)
    dp_table = {}

    def calculate_min_operations(i):
        if (i, arr[i]) in dp_table:
            return dp_table[(i, arr[i])]
        
        if i == 0:
            return 0
        
        min_ops = float('inf')
        
        for j in range(arr[i-1], arr[i] + 1):
            ops = calculate_min_operations(i-1) + (abs(j - arr[i]) if j < arr[i] else 0)
            min_ops = min(min_ops, ops)
        
        dp_table[(i, arr[i])] = min_ops
        return min_ops

    return calculate_min_operations(N-1)

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    print(min_operations(arr))
