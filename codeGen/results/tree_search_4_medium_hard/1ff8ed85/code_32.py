def can_send_over_network(b):
    n = len(b)
    seen = {}
    segment_lengths = []
    
    for val in b:
        if val not in seen:
            seen[val] = 1
        else:
            seen[val] += 1
    
    for val, freq in seen.items():
        segment_lengths.append((val, freq))
    
    for i in range(1, n):
        prev_val, prev_freq = segment_lengths[i-1]
        curr_val = b[i]
        
        if curr_val not in seen:
            return "YES"
        
        curr_freq = seen[curr_val]
        
        while (prev_val + 1) <= curr_val and prev_freq > 0:
            if curr_val - prev_val == curr_freq:
                break
            prev_val += 1
            prev_freq -= 1
        
        if prev_val + prev_freq >= curr_val and curr_freq > 0:
            return "YES"
    
    return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    print("YES" if can_send_over_network(b) else "NO")
