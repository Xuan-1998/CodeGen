import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    
    # Build the frequency map for sequence a
    freq_map = {}
    for x in set(b):
        freq_map[x] = b.count(x)
    
    # Initialize dynamic programming table and segment count
    dp_table = {0: 1}  # Base case: one way to obtain sequence [0]
    segment_count = 1
    
    # Iterate through the sequence b
    for x in b:
        if x not in freq_map or freq_map[x] == 0:
            break
        
        # Update dynamic programming table and segment count
        for i in range(x - 1, -1, -1):
            if i + 1 not in dp_table:
                dp_table[i + 1] = 0
            dp_table[i + 1] += dp_table.get(i, 0)
        
        freq_map[x] -= 1
        segment_count += 1
    
    # Print the result
    if segment_count == len(b):
        print("YES")
    else:
        print("NO")
