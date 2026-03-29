def max_score():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        
        # Initialize our current position and score
        curr_pos = 1
        curr_score = arr[0]
        
        # Initialize the maximum score that can be achieved
        max_score = curr_score
        
        # Perform exactly k moves
        for _ in range(k):
            # Check if we need to move left or right
            while z > 0:
                # Move left until we can't anymore or until our current position is at index 1
                if curr_pos < 2 or (k - _) % (z + 1) != 0:
                    break
                curr_pos -= 1
                curr_score += arr[curr_pos]
                z -= 1
            
            # If we still have moves left, move right
            if z > 0 and _ < k - 1:
                while z > 0:
                    curr_pos += 1
                    curr_score += arr[curr_pos]
                    z -= 1
            
            # Update the maximum score that can be achieved
            max_score = max(max_score, curr_score)
        
        print(max_score)

max_score()
