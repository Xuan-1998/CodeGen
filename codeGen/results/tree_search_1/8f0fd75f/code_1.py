import sys

def can_support(durabilities, distances, new_point_durability):
    # Create a list to store the maximum length each point can support
    max_support = [min(durabilities[i], distances[i+1] - distances[i], distances[i] - distances[i-1]) for i in range(1, len(durabilities) + 1)]
    
    # Add the new point at the beginning with the given durability
    max_support.insert(0, new_point_durability)
    
    # Simulate the process of collapsing
    for i in range(1, len(max_support)):
        # Check if the current point collapses
        if distances[i] - distances[i-1] > max_support[i-1]:
            # Redistribute the load to the next point
            max_support[i] = min(max_support[i], max_support[i-1] - (distances[i] - distances[i-1]))
            if max_support[i] <= 0:
                return False
    return True

def binary_search(durabilities, distances):
    left, right = 0, distances[-1] - distances[0]
    while left < right:
        mid = (left + right) // 2
        if can_support(durabilities, distances, mid):
            right = mid
        else:
            left = mid + 1
    return left

def main():
    n = int(sys.stdin.readline().strip())
    distances = list(map(int, sys.stdin.readline().strip().split()))
    durabilities = list(map(int, sys.stdin.readline().strip().split()))
    
    # If the building doesn't collapse without adding a new point
    if can_support(durabilities, distances, 0):
        print(0)
    else:
        # Find the minimum durability required for the new point
        result = binary_search(durabilities, distances)
        print(result)

if __name__ == "__main__":
    main()
