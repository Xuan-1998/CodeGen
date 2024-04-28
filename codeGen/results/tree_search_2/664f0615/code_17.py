def maximum_path_segment_length():
    initial_speed, final_speed, time, max_diff = map(int, input().split())
    
    tabulation_result = [[0] * (time + 1) for _ in range(max_diff + 1)]
    
    for i in range(1, time + 1):
        for diff in range(1, max_diff + 1):
            if abs(final_speed - initial_speed - diff * (i - 1)) <= max_diff:
                tabulation_result[diff][i] = min(tabulation_result[diff][i-1], i) if i > 0 else i
            else:
                tabulation_result[diff][i] = tabulation_result[diff][i-1]
    
    return max([tabulation_result[i][time] for i in range(max_diff + 1)])

print(maximum_path_segment_length())
