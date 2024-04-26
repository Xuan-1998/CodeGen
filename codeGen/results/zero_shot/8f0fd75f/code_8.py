def read_input():
    n = int(input().strip())
    coordinates = list(map(int, input().strip().split()))
    durability = list(map(int, input().strip().split()))
    return n, coordinates, durability

def simulate_load_distribution(coordinates, durability):
    # This function will simulate the load distribution and return
    # True if the building collapses, False otherwise.
    pass

def binary_search_minimum_durability(n, coordinates, durability):
    # This function will perform a binary search to find the minimum
    # durability required for the new point.
    pass

def main():
    n, coordinates, durability = read_input()
    
    # Check if the building collapses without adding a new point
    if simulate_load_distribution(coordinates, durability):
        # Perform binary search to find the minimum durability needed
        min_durability = binary_search_minimum_durability(n, coordinates, durability)
        print(min_durability)
    else:
        # No new point is needed
        print(0)

if __name__ == "__main__":
    main()
