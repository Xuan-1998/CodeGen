def max_score():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        
        # Initialize maximum score and current score as 0.
        max_score = 0
        curr_score = 0
        
        # Traverse through the array from index 1 to n.
        for i in range(1, n):
            # If we are not allowed to make moves left then add value at next index to current score.
            if k == z:
                curr_score += arr[i]
            else:
                # Traverse right and add value until no more than 'z' moves are left or end of array is reached.
                while k > 0 and i + z <= n:
                    curr_score += arr[i+z-1]
                    k -= 1
                    z -= 1
                
                # Now we have to make exactly 'k' moves, so add value at previous index until no more than 'z' moves are left.
                while k > 0 and i - z >= 1:
                    curr_score += arr[i-z-1]
                    k -= 1
                    z -= 1
                
                # If there is still some move left then use it to add value at previous index.
                if k > 0:
                    curr_score += arr[i-1]
                    
            # Update the maximum score.
            max_score = max(max_score, curr_score)
            
        print(max_score)

max_score()
