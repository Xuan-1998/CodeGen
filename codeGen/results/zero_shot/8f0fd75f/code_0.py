def read_ints():
    return list(map(int, input().split()))

def find_min_durability(n, coords, durability):
    max_durability_needed = 0
    left_load = 0  # Load supported by the point to the left of the current point

    for i in range(1, n + 1):
        # Calculate the length of the segment supported by the current point
        segment_length = coords[i] - coords[i - 1] + left_load
        # If the segment length is greater than the durability of the point, it collapses
        if segment_length > durability[i - 1]:
            # Load is redistributed to the next point
            left_load = segment_length - durability[i - 1]
            # Update the max durability needed for the additional point
            max_durability_needed = max(max_durability_needed, left_load)
        else:
            left_load = 0  # Reset the load if the point can support the segment

    # Check if the last point can support the segment without collapsing
    if left_load > 0:
        max_durability_needed = max(max_durability_needed, left_load)

    return max_durability_needed

def main():
    n = int(input())
    coords = read_ints()
    durability = read_ints()
    min_durability = find_min_durability(n, coords, durability)
    print(min_durability)

if __name__ == "__main__":
    main()
