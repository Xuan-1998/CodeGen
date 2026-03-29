t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    dp = {0: {val: 1 for val in set(b)}}
    current_segment_length = 0
    segment_count = 0
    
    for val in sorted(b):
        if val > current_segment_length:
            current_segment_length += 1
            segment_count += 1
            dp[segment_count] = {k: v.copy() for k, v in dp[current_segment_length-1].items()}
        dp[segment_count][val] += 1
    
    result = "YES" if any(all(dp[i][j] == count for j, count in enumerate(b)) for i in range(1, segment_count+1)) else "NO"
    
    print(result)
