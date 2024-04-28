def max_distance(t, s, start):
    # Base case: if we've reached the end of the segment, return 0
    if t <= 0:
        return 0

    # If we're at the starting point, calculate the maximum distance that can be covered
    # with the initial speed within the remaining time
    if start:
        max_dist = min(t * s, 100)  # assume max allowed change is 10 m/s
    else:  # if we're not at the starting point, use the final speed
        max_dist = min((t + 1) * s, 100)

    # Memoize intermediate results
    memo = {}

    def memoized_max_distance(t, s, start):
        if (t, s, start) in memo:
            return memo[(t, s, start)]

        # Calculate the maximum distance that can be covered at the given speed within the remaining time
        max_dist = min(t * s, 100)

        # Recursively call the function with updated remaining time and speed
        if t > 1:
            max_dist += memoized_max_distance(t - 1, s, not start)
        else:  # we've reached the end of the segment
            return max_dist

        # Store intermediate result in memoization dictionary
        memo[(t, s, start)] = max_dist
        return max_dist

    return memoized_max_distance(t, s, start)

# Example usage:
initial_speed = int(input())
final_speed = int(input())
time = int(input())
max_allowed_change = int(input())

print(max_distance(time, final_speed - initial_speed, 0))
