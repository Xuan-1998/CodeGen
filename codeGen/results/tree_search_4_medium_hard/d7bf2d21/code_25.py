def find_number_of_longest_increasing_subsequences(sequence):
    n = len(sequence)
    dp = [[0, None] for _ in range(n)]

    max_length = 1
    last_element = sequence[0]
    
    for i in range(1, n):
        if sequence[i] > last_element:
            dp[i][0] = dp[i-1][0] + 1
            dp[i][1] = sequence[i]
        else:
            dp[i][0] = max_length
            dp[i][1] = None
        
        if dp[i][0] > max_length:
            max_length = dp[i][0]

    count = 0
    last_element = sequence[0]
    
    for i in range(n):
        if sequence[i] == last_element and dp[i][0] == max_length:
            count += 1
        last_element = dp[i][1]

    return count
