# Step 3: Iterate over views and calculate total brightness
for view in views:
    t, (x1, y1), (x2, y2) = view
    
    # Initialize the total brightness for this view to 0
    total_brightness = 0
    
    # Initialize a variable to keep track of which star we're currently looking at
    current_star_index = 0
    
    # Iterate over each row in the view
    while y1 <= y2:
        # Calculate the x-coordinate of the right edge of this row
        right_edge_x = min(x2, stars[current_star_index][0])
        
        # Add up the brightness of all the stars that are visible in this row
        total_brightness += sum(s for s in stars[current_star_index:] if s[0] <= right_edge_x and s[1] >= y1 and s[1] <= y2)
        
        # Move to the next row
        y1 += 1
        
    print(total_brightness)
