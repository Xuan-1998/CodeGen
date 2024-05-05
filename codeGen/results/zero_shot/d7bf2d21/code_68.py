def count_lis(input_array):
    global lis_count
    dp = [1] * len(input_array)
    
    for i in range(1, len(input_array)):
        for j in range(i):
            if input_array[i] > input_array[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    max_length = max(dp)
    lis_count = sum(1 for x in dp if x == max_length)

    return lis_count

input_array = list(map(int, input().split()))
lis_count = count_lis(input_array)
print(lis_count)
