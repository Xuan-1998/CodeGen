code
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    dp = {i: False for i in range(n+1)}
    state_dict = {}
    
    for i in range(1, n+1):
        segment_length = 0
        for j in range(i):
            if a[j] > a[i-1]:
                break
            segment_length += 1
        if segment_length not in state_dict:
            state_dict[segment_length] = {val: 0 for val in set(a)}
        for val in set(a[:i]):
            state_dict[segment_length][val] += 1
        
    for i in range(1, n+1):
        dp[i] = False
        if a[i-1] > b[i-1]:
            continue
        elif a[i-1] == b[i-1]:
            dp[i] = dp[i-1]
        else:
            prev_segments = [(k, v) for k, v in state_dict.items() if k < i]
            for segment_length, freq in prev_segments:
                new_state = {**state_dict[segment_length], **{val: freq[val]-1 for val in set(a[:i])}}
                if all(val <= b[i-1] and freq[val] > 0 for val in new_state):
                    dp[i] = True
                    break
    
    print('YES' if dp[n] else 'NO')
