def can_send_sequence():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        # Initialize a counter to keep track of used segments
        used_segments = 0
        
        for i in range(1, n):
            # Check if there's a segment that could be split into two segments with lengths equal to the current gap minus one
            if b[i] - b[i-1] == 2 + used_segments:
                used_segments += 1
            elif b[i] - b[i-1] != 2 + used_segments:
                print("NO")
                return
        
        print("YES")

can_send_sequence()
