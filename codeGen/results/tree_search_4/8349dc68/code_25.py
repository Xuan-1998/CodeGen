def max_sum_after_partitioning(arr, k):
    n = len(arr)
    d = {}
    
    def f(i, j, max_sum):
        if (i, j) in d:
            return d[(i, j)]
        
        if i - j <= k:
            d[(i, j)] = max(arr[i-j:i]) + max_sum
        else:
            d[(i, j)] = max(arr[i-j:i]) + f(i-j-1, j-1, max_sum)
        
        return d[(i, j)]
    
    max_sum = 0
    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            max_sum = max(max_sum, f(i, j, 0))
    
    return max_sum

if __name__ == "__main__":
    import sys
    input = sys.stdin.read().strip().split()
    arr = [int(x) for x in input[1:]]
    k = int(input[0])
    print(max_sum_after_partitioning(arr, k))
