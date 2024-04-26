def read_input():
    n = int(input().strip())  # Number of ordinary points
    coords = list(map(int, input().strip().split()))  # Coordinates of all points
    durabilities = list(map(int, input().strip().split()))  # Durabilities of ordinary points
    return n, coords, durabilities

def simulate_collapse(n, coords, durabilities):
    max_segment_length = 0
    segments = [coords[i+1] - coords[i] for i in range(n+1)]  # Initial segments lengths

    # Iterate through the ordinary points
    for i in range(n):
        if segments[i] > durabilities[i]:  # Point collapses
            # Redistribute the load to the neighbors
            if i > 0:  # If not the first point
                segments[i-1] += segments[i] - durabilities[i]
            if i < n-1:  # If not the last point
                segments[i+1] += segments[i] - durabilities[i]
            segments[i] = durabilities[i]

        # Update the maximum segment length
        max_segment_length = max(max_segment_length, segments[i])

    # Check the last segment
    max_segment_length = max(max_segment_length, segments[n])

    return max_segment_length

def main():
    n, coords, durabilities = read_input()
    result = simulate_collapse(n, coords, durabilities)
    print(result)

if __name__ == "__main__":
    main()
