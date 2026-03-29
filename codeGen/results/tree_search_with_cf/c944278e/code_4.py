def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    # Number of elements in the sequence
    total_elements = 2 ** n
    
    # Initialize the sequence p
    p = list(range(1, total_elements + 1))
    
    # Initialize the dp dictionary
    dp = {}
    
    # Base case: dp[0][mask] is initialized to the values directly
    for i in range(total_elements):
        dp[(0, 1 << i)] = {p[i]}
    
    # Transition
    for i in range(n):
        next_dp = {}
        for mask in dp:
            if mask[0] != i:
                continue
            current_set = dp[mask]
            for j in range(0, total_elements, 2 ** (i + 1)):
                for k in range(0, 2 ** i):
                    left_mask = 1 << (j + k)
                    right_mask = 1 << (j + k + 2 ** i)
                    combined_mask = mask[1] & (left_mask | right_mask)
                    if combined_mask == (left_mask | right_mask):
                        new_mask = mask[1] ^ (left_mask | right_mask)
                        if s[i] == '0':
                            new_element = min(p[j + k], p[j + k + 2 ** i])
                        else:
                            new_element = max(p[j + k], p[j + k + 2 ** i])
                        new_mask |= 1 << (p.index(new_element))
                        if (i + 1, new_mask) not in next_dp:
                            next_dp[(i + 1, new_mask)] = set()
                        next_dp[(i + 1, new_mask)].update(current_set)
        
        dp = next_dp
    
    # Result Extraction
    final_mask = 0
    for i in range(total_elements):
        final_mask |= 1 << i
    
    result_set = set()
    for mask in dp:
        if mask[0] == n:
            result_set.update(dp[mask])
    
    # Output the result in sorted order
    result_list = sorted(result_set)
    print(" ".join(map(str, result_list)))


