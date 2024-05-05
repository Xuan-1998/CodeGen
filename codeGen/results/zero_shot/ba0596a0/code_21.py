def can_cross_road(stones):
    # Initialize the current position to 0 (the starting point)
    current_position = 0

    for i in range(1, len(stones)):
        # Calculate the distance between the current stone and the next stone
        distance = stones[i] - stones[i-1]

        # Check if the frog can reach the next stone from the current position
        if (distance < 2 or distance > 3) and current_position != 0:
            return False

        # Update the current position to the new stone's position
        current_position = stones[i]

    return True

# Example usage
stones = [0, 1, 3, 5, 7, 10]
print(can_cross_road(stones))  # Output: True
