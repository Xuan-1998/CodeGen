import sys

def find_min_city_area():
    n = int(sys.stdin.readline())
    
    # Read the coordinates of the mines from stdin
    mines = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        mines.append((x, y))
    
    # Calculate the minimum and maximum x-coordinates
    min_x = min(x for x, y in mines)
    max_x = max(x for x, y in mines)
    
    # Calculate the minimum and maximum y-coordinates
    min_y = min(y for x, y in mines)
    max_y = max(y for x, y in mines)
    
    # Calculate the side length of the city
    side_length = max(max_x - min_x, max_y - min_y)
    
    # Print the minimum possible area of the city
    print(side_length ** 2)

if __name__ == "__main__":
    find_min_city_area()
