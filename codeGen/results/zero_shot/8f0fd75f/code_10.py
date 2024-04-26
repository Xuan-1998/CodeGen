def read_input():
    n = int(input())  # Number of ordinary points
    coordinates = list(map(int, input().split()))  # Coordinates of all points including the bearing points
    durabilities = list(map(int, input().split()))  # Durabilities of ordinary points
    return n, coordinates, durabilities

def main():
    n, coordinates, durabilities = read_input()
    
    # TODO: Implement the solution here
    
    # Placeholder for the actual output
    print(0)

if __name__ == "__main__":
    main()
