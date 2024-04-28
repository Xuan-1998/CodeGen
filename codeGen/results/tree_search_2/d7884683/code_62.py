def partition_times(arr):
    memo = {}
    
    def helper(index, partition_count):
        if index >= len(arr):
            return 0
        if (index, partition_count) in memo:
            return memo[(index, partition_count)]
        
        left_sum = sum(arr[:index+1])
        right_sum = sum(arr[index+1:])
        
        if left_sum == right_sum:
            memo[(index, partition_count)] = 1 + helper(index+2, partition_count)
        else:
            memo[(index, partition_count)] = max(helper(index+1, partition_count), 
                                                 helper(index+2, partition_count))
        
        return memo[(index, partition_count)]
    
    return helper(0, 0)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(partition_times(arr))

if __name__ == "__main__":
    main()
